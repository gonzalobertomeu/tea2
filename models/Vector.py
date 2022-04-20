from mongoengine import *

class Vector(Document):
    x = IntField(require=True)
    y = IntField(require=True)