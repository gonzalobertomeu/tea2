from mongoengine import *

class Video(Document):
    cantFrames = IntField(require=True)
    file = StringField(required=True)
    processed = StringField()