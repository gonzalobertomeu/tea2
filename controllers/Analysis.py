from models.Estudio import Estudio
from models.Usuario import Usuario
from models.Medico import Medico
from models.Video import Video
from models.Frame import Frame
from models.Gestos import Gesto
from models.Vector import Vector

import math
import json

import mongoengine as m
m.connect(db="tea-db",host="localhost",port=27017)

estudio = Estudio.objects(id="5d6ee2dec0375a8bbf40ec97").first()

print(estudio.video.cantFrames)
print(estudio.id)

frames = Frame.objects(estudio=estudio.id)

analisis = dict()
for g in estudio.gestos:
    modulos = []
    for f in frames:
        x = f.vectores[g.fin].x - f.vectores[g.inicio].x
        y = f.vectores[g.fin].y - f.vectores[g.inicio].y
        m = round(math.sqrt(pow(x,2)+pow(y,2)),2)
        print(m)
        modulos.append(m)
    analisis[g.descripcion] = modulos

file = open("Analisis 1.txt","w")
file.write(json.dumps(analisis,indent=4))
file.close()
    