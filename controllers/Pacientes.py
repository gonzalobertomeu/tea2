from models.Usuario import Usuario

def crearPaciente(nombre,apellido,dni,fechaNac,sexo,nacionalidad):
    #Hacer validaciones necesarias...
    print("Creacionnnn",nombre,apellido,dni,fechaNac,sexo,nacionalidad)
    if ( nombre == "" ):
        return None
    
    if ( apellido == "" ):
        return None
    
    if ( dni == "" ):
        return None

    if ( fechaNac == "" ):
        return None

    if ( sexo == "" ):
        return None
    
    if ( nacionalidad == "" ):
        return None
    
    #Asignaciones
    nuevo = Usuario()
    nuevo.nombre = nombre
    nuevo.apellido = apellido
    nuevo.dni = dni
    nuevo.fechaNac = fechaNac
    nuevo.sexo = sexo
    nuevo.nacionalidad = nacionalidad

    return nuevo.save()
     

def buscarAllPacientes():
    pacientes = Usuario.objects()
    return pacientes

def buscarPacientePorDni(dni):
    paciente = Usuario.objects(dni__exact=dni).first()
    return paciente
    
def buscarPacientesPorApellido(apellido):
    if(apellido == ""):
        return None
    pacientes = Usuario.objects(apellido__icontains=apellido)
    return pacientes