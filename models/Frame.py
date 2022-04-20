from mongoengine import *

class Frame(Document):
    nFrame = IntField(required=True)
    estudio = ReferenceField('Estudio')
    vectores = ListField(ReferenceField('Vector'))