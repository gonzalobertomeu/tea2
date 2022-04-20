from mongoengine import *
from Gestos import Gesto
from Vector import Vector

connect(db='tea-db',host='172.17.0.2',port=27017)


# sonrisa = Gesto.objects(descripcion="sonrisa").first()

# print(sonrisa.descripcion)
# print(sonrisa.inicio.y)
# print(sonrisa.fin.y)



# vector1 = Vector(x=10,y=3)
# vector2 = Vector()
# vector2.x = 7
# vector2.y = 45

# vector1.save()
# vector2.save()

# gesto1 = Gesto()

# gesto1.descripcion = "sonrisa"
# gesto1.inicio = vector1
# gesto1.fin = vector2

# gesto1.save()