import cv2 as vision
import dlib as worker
import uuid
import threading
import time
import sys
import os
import glob
import pathlib
import math
import controllers.Gestos as Gestos
from mongoengine import connect

connect(db="tea-db",host="172.17.0.2",port=27017)

def shape_to_event(shape):              #transforma lo obtenido del shape_predictor a Eventos
    event = []                          #vector de coordenadas -> Cada evento tiene 68 coordenadas (x,y)
    for i in range(0,68):               #lleno el evento con las coordenadas del shape
        coord = (shape.part(i).x,shape.part(i).y)
        event.append(coord)
    return event

gestos = Gestos.buscarAllGestos()

face_folder_path = sys.argv[1]
path = pathlib.Path().absolute()
print(path)
detector = worker.get_frontal_face_detector()     #inicializo detector de caras
predictor = worker.shape_predictor("assets/sp_68.dat") #inicializo el predictor de formas con el archivo preentrenado './sp_68.dat'
for f in glob.glob(os.path.join(face_folder_path,"*.*")):
    filename = f.split('/')[1].split('.')[0]
    print(filename)
    image = vision.imread(f)
    gray = vision.cvtColor(image,vision.COLOR_BGR2GRAY)       #paso el fotograma a blanco y negro
    gray = vision.equalizeHist(gray)                       #normalizo el fotograma (mejor contraste y brillo)
    dets = detector(gray,1)
    vectoreventos = [] 
    faceSize = 0                        #detecto las caras dentro del fotograma
    for face in dets: 
        faceSize = round(math.sqrt((face.bl_corner().x-face.tr_corner().x)**2+(face.bl_corner().y-face.tr_corner().y)**2),2)     
        print('Face size = {}'.format(faceSize))                        #recorro las caras de la imagen
        shape = predictor(gray,face)                   #obtengo la forma de la cara (68 puntos)
        event = shape_to_event(shape)                   #paso de shape a evento (vector de coordenadas)
        vectoreventos.append(event)
        for point in event:                               #recorro la forma -> cada ciclo corresponde a un punto
            #print(point)                          #muestro por consola las coordenadas de cada punto procesado               
            vision.circle(image,point,1,(0,255,255),-1)

    document = open('/home/jose/Develop/py/tea-models/editedfaces/gestos-'+filename+'.txt',newline='',encoding='utf-8',mode='w')
    document.write('[Gesto] > (Modulo)'+os.linesep)
    for ve in vectoreventos:
        print(len(ve))
        for g in gestos:
            inicio = g.inicio - 1
            fin = g.fin - 1
            modulo = math.sqrt((ve[inicio][0]-ve[fin][0])**2+(ve[inicio][1]-ve[fin][1])**2)
            text = '[{}] > ({}){}'.format(g.descripcion,round(modulo/faceSize*100,2), os.linesep)
            document.write(text)
            vision.line(image,ve[inicio],ve[fin],(0,255,0),1)

    document.close()
    #vision.imshow('image',image)
    vision.imwrite('/home/jose/Develop/py/tea-models/edited'+f,image)
    vision.waitKey(0)