from models.Estudio import Estudio
from models.Frame import Frame
from models.Usuario import Usuario
from models.Medico import Medico
from models.Video import Video
from models.Gestos import Gesto
from models.Vector import Vector

from mongoengine.queryset.visitor import Q

import csv
import datetime
import math



def getCSVByEstudio():
    date = datetime.datetime.now().strftime("%d-%m-%y")

    estudios = Estudio.objects(estado=2)
    for e in estudios:
        with open('csv/'+e.paciente.apellido+e.paciente.nombre+' '+date+'.csv','w') as file:
            file = csv.writer(file,delimiter=',',quoting=csv.QUOTE_MINIMAL)
            
            firstRow = ['nFrame']
            for g in e.gestos:
                firstRow.append(g.descripcion)
            file.writerow(firstRow)

            frames = Frame.objects(estudio=e.id)
            for f in frames:
                newRow = [f.nFrame]
                for g in e.gestos:
                    p1 = f.vectores[g.inicio]
                    p2 = f.vectores[g.fin]
                    modulus = math.sqrt(math.pow(p2.x-p1.x,2)+math.pow(p2.y-p1.y,2))
                    newRow.append(modulus)
                file.writerow(newRow)

def getCSVallEstudio():
    date = datetime.datetime.now().strftime("%d-%m-%y")
    estudios = Estudio.objects(estado=2)
    gestos = Gesto.objects()

    for g in gestos:
        with open('csv/gestos/'+g.descripcion+'.csv','w') as dump:
            dump = csv.writer(dump, delimiter=',')
            
            firstRow=['nFrame']
            for e in estudios:
                firstRow.append(e.paciente.apellido+e.paciente.nombre)
            dump.writerow(firstRow)
            print("First row processed")

            nFrame = 0
            while True:
                print("Processing: {}".format(nFrame))
                nextRow = []
                nextRow.append(nFrame)

                for e in estudios:
                    frame = Frame.objects(Q(estudio=e.id) & Q(nFrame=nFrame)).first()
                    if frame:
                        p1 = frame.vectores[g.inicio]
                        p2 = frame.vectores[g.fin]
                        modulus = math.sqrt(math.pow(p2.x-p1.x,2)+math.pow(p2.y-p1.y,2))
                    else:
                        modulus = 'error'
                    nextRow.append(modulus)
                #print(nextRow)
                nFrame += 1
                dump.writerow(nextRow)
                if nFrame == 5628:
                    break