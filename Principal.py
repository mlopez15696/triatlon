from Triatlon import Triatlon
resultados=None


def registroEquipos():
    print("1.  Registrar Primer Equipo")
    print("2.  Registrar Segundo Equipo")
    print("3.  Salir")

while True:
    print("\n\n Bienvenidos al Triatlon \n")
    print("1.   Registros de Equipos")
    print("2.   Iniciar Competencia")
    print("3.   Resultados de la Competencia")
    print("4.   Salir")
    opcionMenu = input("Inserta un opcion: ")

    if opcionMenu=="1":
        print("Registros de Participantes al Triatlon ")
        registroEquipos()
        opcionMenu2 = input("Ingrese la opcion a elegir: ")
        if opcionMenu2 =="1":
         print("----------------------------PRIMER EQUIPO----------------------------")
         mtsPorMinutoNatacion=int(input("Ingrese la velocidad promedio de metros*minuto en natacion del primer miembro del equipo: "))
         mtsPorMinutoCiclismo=int(input("Ingrese la velocidad promedio de metros*minuto en Ciclismo el segundo miembro del equipo: "))
         mtsPorMinutoCorriendo=int(input("Ingrese la velocidad promedio de metros*minuto corriendo del tercer miembro del equipo: "))
         primerEquipo = Triatlon(mtsPorMinutoNatacion,mtsPorMinutoCiclismo,mtsPorMinutoCorriendo)

        if opcionMenu2=="2":
            print("----------------------------SEGUNDO EQUIPO----------------------------")
            mtsPorMinutoNatacion = int( input("Ingrese la velocidad promedio de metros*minuto en natacion del primer miembro del equipo: "))
            mtsPorMinutoCiclismo = int(input("Ingrese la velocidad promedio de metros*minuto en Ciclismo el segundo miembro del equipo: "))
            mtsPorMinutoCorriendo = int(input("Ingrese la velocidad promedio de metros*minuto corriendo del tercer miembro del equipo: "))
            segundoEquipo = Triatlon(mtsPorMinutoNatacion, mtsPorMinutoCiclismo, mtsPorMinutoCorriendo)
        if opcionMenu2=="3":
            break

    elif opcionMenu=="2":
        print("-----------------------INICIANDO CARRERA----------------------------")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("--------------------PRIMER EQUIPO----------------------------")
        primerEquipo.Natacion()
        primerEquipo.Ciclismo()
        primerEquipo.Corriendo()
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("--------------------SEGUNDO EQUIPO----------------------------")
        segundoEquipo.Natacion()
        segundoEquipo.Ciclismo()
        segundoEquipo.Corriendo()

    elif opcionMenu=="3":
        print("--------------------RESULTADOS COMPETENCIA----------------------------")
        primerEquipo.Resultados()
        segundoEquipo.Resultados()
        print("El tiempo del primer Equipo es : " + str(primerEquipo.resultadoEquipos) + " minutos y segundos")
        print("El tiempo del segundo Equipo es :" + str (segundoEquipo.resultadoEquipos) + " minutos y segundos")

        if primerEquipo.resultadoEquipos< segundoEquipo.resultadoEquipos:
            print()
            print("El equipo ganador es el Primer equipo con: " + str(primerEquipo.resultadoEquipos) + " minutos y segundos")
        else:
            print("El ganador es el Segundo Equipo con: " + str(segundoEquipo.resultadoEquipos) + " minutos y segundos")

    elif opcionMenu=="4":
        break

    else:
        print("")
        input("No has ingresado niguna opcion correcta")