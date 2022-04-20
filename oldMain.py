def logo():
    print("     TEA     ")

def menu():
    print("1 - Realizar estudio")
    print("2 - Consultar estudio")
    print("3 - ABM Paciente")
    print("4 - ABM Medico")
    print("5 - ABM Gestos")
    sel = input("Seleccione una opcion: ")
    if(sel=="1"):
        #realiza estudio
        print(sel)
    if(sel=="2"):
        #consulta estudio3
        print(sel)
    if(sel=="3"):
        #ABM paciente
        abm_pacientes()
    if(sel=="4"):
        #ABM Medico
        print("Selecciono 4")
    if(sel=="5"):
        #ABM Gesto
        print(sel)
    else:
        print("Error al seleccionar")
        menu()


def abm_pacientes():
    print("1 - Nuevo paciente")
    print("2 - Eliminar paciente (NI)")
    print("3 - Modificar paciente (NI)")
    sel = input("Selecciones una opcion: ")
    if(sel == "1"):
        #alta
        print(sel)
    if(sel == "2"):
        #baja
        print(sel)
    if(sel == "3"):
        #modificaciones
        print(sel)
    else:
        print("Error al seleccionar")
        abm_pacientes()


def main():
    logo()
    menu()


main()

