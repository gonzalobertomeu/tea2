import cv2 as vision
import dlib as worker
import uuid
import threading
import time
import tkinter as Tk

videoshared = []
frameshared = 1
hilos = []
out = None
end = False

def getCamara():
    camaras = [3,2,1,0]
    for c in camaras:
        camara = vision.VideoCapture(c)
        if not camara.isOpened():
            continue
        else:
            return camara

def capturarVideo(name):
    vision.namedWindow('TEA',vision.WND_PROP_FULLSCREEN)
    vision.setWindowProperty('TEA',vision.WND_PROP_FULLSCREEN,vision.WINDOW_FULLSCREEN)
    
    #Fotogramas en RAM
    global videoshared
    global frameshared
    global hilos
    global end
    id = ''
    global out
    #Set camara
    camara = getCamara()
    camara.set(vision.CAP_PROP_FPS,30)
    player = vision.VideoCapture('assets/TEA4.mp4')
    player.set(vision.CAP_PROP_FPS,30)
    camara.set(vision.CAP_PROP_FRAME_WIDTH,640)
    camara.set(vision.CAP_PROP_FRAME_HEIGHT,480)
    
    out,id = startWriting(name)
    y = threading.Thread(target=writeControl)
    y.start()
    hilos.append(y)
    while player.isOpened():
        ret,reactions = player.read()
        if not ret:
            break
        vision.imshow('TEA',reactions)
        ret, pic = camara.read()
        if not ret:
            break
        videoshared.append({'pic': pic,'n': frameshared})
        frameshared += 1
        if vision.waitKey(1) == ord('q'):
            break
    end = True
    x = threading.Thread(target=writeFrames,args=(out,videoshared))
    x.start()
    hilos.append(x)
    print("Esperando hilos")
    for t in hilos:
        t.join()
    ret, file = finishWriting(out,name,id)
    if not ret:
        print("Error al finalizar la grabacion")
    out = None
    videoshared = []
    hilos = []
    camara.release()
    player.release()
    vision.destroyAllWindows()
    print("Grabacion terminada")
    return True,file,frameshared

def calibrarCamara():
    camara = getCamara()
    if ( not camara.isOpened() ):
        print('no se pudo abrir la camara')
        return False
    else: 
        vision.namedWindow('Calibrar Camara')

    while True:
        ret, frame = camara.read()
        if not ret:
            print('Error al capturar')
            return False
        vision.imshow('Calibrar Camara',frame)
        if vision.waitKey(1) == ord('q'):
            break
    camara.release()
    vision.destroyAllWindows()

def startWriting(name):
    print("Empieza a grabar")
    id = uuid.uuid4().hex
    fourcc = vision.VideoWriter_fourcc('M','P','E','G')    #codecs de video para guardar el archivo
    out = vision.VideoWriter('estudios/{}{}.avi'.format(name,id),fourcc,23,(640,480))     #se inicializa el escritor de video
    return out, id

def finishWriting(out,name,id):
    print("Cerrando la grabacion")
    out.release()
    f = open('estudios/{}{}.avi'.format(name,id))
    file = f.name
    f.close()
    return True,file

def writeFrames(out,frames):
    print("Thread grabando fotogramas")
    for image in frames:                 #recorro el video
        if not out.isOpened():
            return False
        out.write(image['pic'])
    print("300 FOTOGRAMAS FUERON GRABADOS!!!!!")

def writeControl():
    global videoshared
    global frameshared
    global out
    global hilos
    global end
    while not end:
        if(frameshared % 1000 == 0):
            frames = videoshared[0:1000]
            x = threading.Thread(target=writeFrames,args=(out,frames))
            time.sleep(400/100)
            x.start()
            hilos.append(x)
            del videoshared[0:1000]
        
def shape_to_event(shape):              #transforma lo obtenido del shape_predictor a Eventos
    event = []                          #vector de coordenadas -> Cada evento tiene 68 coordenadas (x,y)
    for i in range(0,68):               #lleno el evento con las coordenadas del shape
        coord = (shape.part(i).x,shape.part(i).y)
        event.append(coord)
    return event

def procesarvideo(estudioId,cb,cbmax):               #funcionalidad principal del sistema
    print("ID : {}".format(estudioId))
    import controllers.Video as cVideo
    import controllers.Estudio as cEstudio
    import views.progress as Progress

    estudio = cEstudio.getEstudioById(estudioId)

    file = cVideo.getVideo(estudio.video.id)

    if file == None:
        print("Error")
        return False
    else:
        print("El archivo id: {}".format(file.id))
        player = vision.VideoCapture(file.file)
        fourcc = vision.VideoWriter_fourcc('M','P','E','G')
        uri = 'estudios/procesados/{}.avi'.format(file.id)
        writer = vision.VideoWriter(uri,fourcc,23,(640,480))

        detector = worker.get_frontal_face_detector()     #inicializo detector de caras
        predictor = worker.shape_predictor("assets/sp_68.dat") #inicializo el predictor de formas con el archivo preentrenado './sp_68.dat'

        #progress.setMaximo(file.cantFrames)
        totalFrames = file.cantFrames
        cbmax(totalFrames)

        vectoreventos = []                  #vector que contiene eventos / cada elemento corresponde a un fotograma             

        from models.Frame import Frame
        from models.Vector import Vector


        index = 0 
        while player.isOpened():
            print("WIP Frame {} - {}%".format(index, (index/totalFrames)*100))
            ret,image = player.read()
            if not ret:
                break
            gray = vision.cvtColor(image,vision.COLOR_BGR2GRAY)       #paso el fotograma a blanco y negro
            gray = vision.equalizeHist(gray)                       #normalizo el fotograma (mejor contraste y brillo)
            dets = detector(gray,1)                            #detecto las caras dentro del fotograma
            for face in dets:                                   #recorro las caras de la imagen
                shape = predictor(gray,face)                   #obtengo la forma de la cara (68 puntos)
                event = shape_to_event(shape)                   #paso de shape a evento (vector de coordenadas)
                vectoreventos.append(event)         
                frame = Frame()
                frame.nFrame = index
                frame.estudio = estudio    
                for point in event:                               #recorro la forma -> cada ciclo corresponde a un punto
                    #print(point)                          #muestro por consola las coordenadas de cada punto procesado
                    punto = Vector()
                    punto.x = point[0]
                    punto.y = point[1]
                    punto.save()   
                    frame.vectores.append(punto)               
                    vision.circle(image,point,1,(0,255,255),-1)
                frame.save()
            writer.write(image)
            index += 1
            cb(1)
        file.processed = uri
        file.save()
        estudio.estado = 2
        estudio.save()
            #progress.updateProgress(index)

        # for index,image in enumerate(video):                    #recorro el video -> cada ciclo correponde a un fotograma
        #     print("WIP Frame {}".format(index))
        #     gray = vision.cvtColor(image,vision.COLOR_BGR2GRAY)       #paso el fotograma a blanco y negro
        #     gray = vision.equalizeHist(gray)                       #normalizo el fotograma (mejor contraste y brillo)
        #     dets = detector(image,1)                            #detecto las caras dentro del fotograma
        #     for face in dets:                                   #recorro las caras de la imagen
        #         shape = predictor(image,face)                   #obtengo la forma de la cara (68 puntos)
        #         event = shape_to_event(shape)                   #paso de shape a evento (vector de coordenadas)
        #         vectoreventos.append(event)                     
        #         for point in event:                               #recorro la forma -> cada ciclo corresponde a un punto
        #             #print(point)                                  #muestro por consola las coordenadas de cada punto procesado
        #             vision.circle(image,point,1,(0,255,255),-1)      #dibujo un circulo en la imagen, con las coordenadas del punto
        # return video,vectoreventos                              #retorno el video nuevo con los puntos dibujados, y el vector de eventos para
                                                            #despues procesar los gestos

