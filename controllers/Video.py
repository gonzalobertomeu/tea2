from models.Video import Video

def getVideo(id):
    print("El parametro id del video: {}".format(id))
    video = Video.objects(id=id).first()
    return video

def getAllVideo():
    return Video.objects()