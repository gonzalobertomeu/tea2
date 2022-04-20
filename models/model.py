from mongoengine import *

connect(db='tea-db',host='172.17.0.2',port=27017)

class Lista(Document):
    texto = SortedListField(ReferenceField('Item'))

class Item(Document):
    descripcion = StringField()

nuevaLista = Lista()

nuevaLista.texto.append(Item(descripcion="Gonzalo").save())
nuevaLista.texto.append(Item(descripcion="Gabriel").save())
nuevaLista.texto.append(Item(descripcion="Bertomeu").save())

nuevaLista.save()

