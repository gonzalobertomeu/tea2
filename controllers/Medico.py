from models.Medico import Medico

def crearMedico(nombre,apellido,especialidad,matricula):
    if (nombre == ""):
        return None
    if (apellido == ""):
        return None
    if (especialidad == ""):
        return None
    if (matricula == ""):
        return None
    
    nuevo = Medico()
    nuevo.nombre = nombre
    nuevo.apellido = apellido
    nuevo.especialidad = especialidad
    nuevo.matricula = matricula
    
    return nuevo.save()
    
def buscarAllMedicos():
    return Medico.objects()

def buscarMedicoPorMatricula(matricula):
    medico = Medico.objects(matricula__exact=matricula).first()
    return medico

def buscarMedicosPorApellido(apellido):
    if(apellido == ""):
        return None
    medicos = Medico.objects(apellido__icontains=apellido)
    return medicos