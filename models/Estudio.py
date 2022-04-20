from mongoengine import *

class Estudio(Document):
    fecha = DateTimeField()
    paciente = ReferenceField('Usuario')
    medico = ReferenceField('Medico')
    video = ReferenceField('Video')
    gestos = ListField(ReferenceField('Gesto'))
    estado = IntField()
    