from models.Gestos import Gesto

def crearGesto(descripcion,inicio,fin):
    
    inicio = int(inicio)
    fin = int(fin)
    if ( descripcion == "" ):
        return None
    if ( (inicio <= 0) or (inicio > 68) ):
        return None
    if ( (fin <= 0) or (fin > 68) ):
        return None
    if ( inicio == fin ):
        return None

    nuevo = Gesto()
    nuevo.descripcion = descripcion
    nuevo.inicio = inicio
    nuevo.fin = fin

    return nuevo.save()

def buscarAllGestos():
    return Gesto.objects()

def buscarById(id):
    if (id != None):
        return Gesto._objects(_id__exact=id)   
    else:
        return None