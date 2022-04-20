from models.Estudio import Estudio
from models.Video import Video
from models.Frame import Frame
from mongoengine.queryset.visitor import Q
import datetime as dt
import numpy as np
import controllers.ComputerVision as cv

def comenzarEstudio(paciente,medico,gestos):
    print("Se comienza el estudio")

    nuevoEstudio = Estudio()
    nuevoEstudio.paciente = paciente
    nuevoEstudio.medico = medico
    nuevoEstudio.gestos = gestos
    nuevoEstudio.estado = 1
    nuevoEstudio.fecha = dt.datetime.now()

    ret, file, nframe = cv.capturarVideo("{}{}".format(paciente.apellido,medico.apellido))
    if not ret:
        print("Error en algo del video")
    else:
        print('Se capturo bien')
    
    estudioVideo = Video()
    estudioVideo.cantFrames = nframe

    estudioVideo.file = file
    estudioVideo.save()

    nuevoEstudio.video = estudioVideo
    nuevoEstudio.save()
    print("Todo se grabo correctamente")
    return True

def imageToBytes(image):
    bytes = image.tobytes()
    return bytes

def bytesToImage(bytes):
    image = np.frombuffer(bytes,dtype=np.uint8)
    image = np.reshape(image, newshape=[480,640,3])
    return image

def testVideoFromEstudio():
    estudio = Estudio.objects().first()
    video = estudio.video
    frames = Frame.objects(video=video)
    images = []
    for f in frames:
        img = {
            'n': f.nFrame,
            'pic': bytesToImage(f.image)
        }
        images.append(img)
    cv.reproducirvideo(images)

def calibrar():
    cv.calibrarCamara()

def getEstudioById(id):
    return Estudio.objects(id=id).first()

def getAllEstudios(estado = False, apellido = False):
    print("Estado: {}".format(estado))
    if not estado:
        if not apellido:
            return Estudio.objects()
        else:
            return Estudio.objects(apellido__icontains=apellido)
    else: 
        if not apellido:
            return Estudio.objects(estado=1)
        else:
            return Estudio.objects(Q(estado=1) & Q(apellido__icontains=apellido))
