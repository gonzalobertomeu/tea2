from mongoengine import * 

class Medico(Document):
    nombre = StringField(required=True)
    apellido = StringField(required=True)
    especialidad = StringField(required=True)
    matricula = StringField(required=True)