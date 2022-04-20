import controllers.MatLab as ctrl
from mongoengine import connect

connect(db="tea-db",host="172.17.0.2",port=27017)
#ctrl.getCSVByEstudio()
ctrl.getCSVallEstudio()