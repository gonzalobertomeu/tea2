from mongoengine import *

class Usuario(Document):
    nombre = StringField(required=True)
    apellido = StringField(required=True)
    dni = StringField(required=True)
    fechaNac = StringField(required=True)
    sexo = StringField(required=True)
    nacionalidad = StringField(required=True)