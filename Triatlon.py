import os
class Triatlon():
    mtsPorMinutoNatacion = 0
    mtsPorMinutoCiclismo = 0
    mtsPorMinutoCorriendo = 0
    resultadosNatacion = 0
    resultadosCiclismo = 0
    resultadosCorriendo = 0
    resultadoEquipos = 0

    def __init__(self, mtsPorMinutoNatacion, mtsPorMinutoCiclismo, mtsPorMinutoCorriendo):
        self.mtsPorMinutoNatacion = mtsPorMinutoNatacion
        self.mtsPorMinutoCiclismo = mtsPorMinutoCiclismo
        self.mtsPorMinutoCorriendo = mtsPorMinutoCorriendo

    def getmtsPorMinutoNatacion(self):
        return self.mtsPorMinutoNatacion

    def getmtsPorMinutoCiclismo(self):
        return self.mtsPorMinutoCiclismo

    def getmtsPorMinutoCorriendo(self):
        return self.mtsPorMinutoCorriendo

    def getresultadosNatacion(self):
        return self.resultadosNatacion

    def getresultadosCiclismo(self):
        return self.resultadosCiclismo

    def getresultadosCorriendo(self):
        return self.resultadosCorriendo

    def getresultadoEquipos(self):
        return self.resultadoEquipos

    def Natacion(self):
        self.resultadosNatacion = 1000 / self.mtsPorMinutoNatacion
        recorrido = 0
        restanteNatacion = 1000
        print("La distancia a recorrer es de 1km nadando")
        if recorrido < 1000:
            print("Le faltan por recorrer: " + str(restanteNatacion) + " mts en natacion")
            for recorrido in range(0, 1000, self.mtsPorMinutoNatacion):
                restanteNatacion = restanteNatacion - self.mtsPorMinutoNatacion
                if restanteNatacion < 0:
                    restanteNatacion = 0
                    print("Le faltan por recorrer: " + str(restanteNatacion) + "mts en natacion")
                else:
                    print("Le faltan por recorrer: " + str(restanteNatacion) + "mts en natacion")
        print("Finalizo la etapa")
        print("\nEl tiempo resultante del primer miembro en natacion es de: " + "{0:.3f}".format(
            self.resultadosNatacion) + " minutos")
        os.system("pause")

    def Ciclismo(self):
        self.resultadosCiclismo = 20000 / self.mtsPorMinutoCiclismo
        recorrido = 0
        restanteCiclismo = 20000
        print("\n----------------------------------------------------")
        print("La distancia a recorrer es de 20km en bicicleta")
        if recorrido < 20000:
            print("Le faltan por recorrer: " + str(restanteCiclismo) + " mts en Ciclismo")
            for recorrido in range(0, 20000, self.mtsPorMinutoCiclismo):
                restanteCiclismo = restanteCiclismo - self.mtsPorMinutoCiclismo
                if restanteCiclismo < 0:
                    restanteCiclismo = 0
                    print("Le faltan por recorrer: " + str(restanteCiclismo) + "mts en Ciclismo")
                else:
                    print("Le faltan por recorrer: " + str(restanteCiclismo) + "mts en Ciclismo")
        print("Finalizo la etapa")
        print("\nEl tiempo resultante del segundo miembro en ciclismo es de: " + "{0:.3f}".format(
            self.resultadosCiclismo) + " minutos")
        os.system("pause")


    def Corriendo(self):
        self.resultadosCorriendo = 10000 / self.mtsPorMinutoCorriendo
        recorrido = 0
        restanteCorriendo = 10000
        print("\n----------------------------------------------------")
        print("La distancia a recorrer es de 10km corriendo")
        if recorrido < 10000:
            print("Le faltan por recorrer: " + str(restanteCorriendo) + " mts Corriendo")
            for recorrido in range(0, 10000, self.mtsPorMinutoCorriendo):
                restanteCorriendo = restanteCorriendo - self.mtsPorMinutoCorriendo
                if restanteCorriendo < 0:
                    restanteCorriendo = 0
                    print("Le faltan por recorrer: " + str(restanteCorriendo) + "mts Corriendo")
                else:
                    print("Le faltan por recorrer: " + str(restanteCorriendo) + "mts Corriendo")
        print("Finalizo la etapa")
        if restanteCorriendo == 0:
            print("Ha terminado la carrera de triatlon")
        print("El tiempo resultante del tercer miembro corriendo es de: " + "{0:.3f}".format(
            self.resultadosCorriendo) + " minutos")
        os.system("pause")

    def Resultados(self):
        self.resultadoEquipos = self.resultadosNatacion + self.resultadosCiclismo + self.resultadosCorriendo
