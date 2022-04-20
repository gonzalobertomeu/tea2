from mongoengine import *

class Gesto(Document):
    descripcion = StringField(required=True)
    inicio = IntField(required=True)
    fin = IntField(required=True)