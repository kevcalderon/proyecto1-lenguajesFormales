import sys
from ControladorAFD import crearAFD, cargarArchivo, guardarArchivoAFD, generarReporte, generarGramatica, evaluarCadena
from ControladorGramatica import crearGramatica, crearArchivoGramatica, generarReporteGramatica, cargarArchivoGramatica
def menuPrincipal():
    while True:
        print("")
        print("*********************")
        print("    MENU PRINCIPAL   ")
        print("*********************")
        print("1.Modulo AFD")
        print("2.Modulo de gramaticas regulares")
        print("3.Acerca de...")
        print("0.Salir")
        try:
            print("")
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            opcion = 5
        
        if opcion in range (0,4):
            if opcion == 1:
                moduloADF()
            elif opcion == 2: 
                moduloGramatica()
            elif opcion == 3:
                acercaDe()
            elif opcion == 0:
                sys.exit()
        else:
            print("")
            print("Opcion invalida, intente de nuevo :D")        
            print("")





def acercaDe():
    print("")
    print("***********************************************")
    print("LENGUAJES FORMALES Y DE PROGRAMACION")
    print("Catedratica: Inga. Zulma Karina Aguirre Ordonez")
    print("Aux: Danilo Urías Coc")
    print("Seccion: B")
    print("***********************************************")
    print("")



def moduloADF():
    while True:
        print("")
        print("*********************")
        print("     MODULO AFD      ")
        print("*********************")
        print("1.Crea AFD")
        print("2.Cargar archivo")
        print("3.Evaluar cadena")
        print("4.Guardar AFD en archivo")
        print("5.Generar reporte AFD")
        print("6.Generar gramatica regular")
        print("0.Regresar al menu principal")
        try:
            print("")
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            opcion = 8
        
        if opcion in range (0,7):
            if opcion == 1:
                crearAFD()
            elif opcion == 2:
                cargarArchivo()
            elif opcion == 3:
                print("")
                # print("En proceso :(")
                menuEvaluarCadena()
            elif opcion == 4:
                guardarArchivoAFD()
            elif opcion == 5:
                generarReporte()
            elif opcion == 6:
                generarGramatica()
            elif opcion == 0:
                menuPrincipal()
        else:
            print("")
            print("Opcion invalida, intente de nuevo :D")        
            print("")


def menuEvaluarCadena():
    while True:
        print("")
        print("*************************")
        print("     EVALUAR CADENA      ")
        print("*************************")
        print("1.Validar una cadena")
        print("2.Ruta en AFD")
        print("0.Regresar al menu principal")
        try:
            print("")
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            opcion = 4
        if opcion in range (0,3):
            if opcion == 1:
                evaluarCadena()
            elif opcion == 2:
                print("En proceso :c")
            elif opcion == 0:
                menuPrincipal()
        else:
            print("")
            print("Opcion invalida, intente de nuevo :D")        
            print("")



def moduloGramatica():
    while True:
        print("")
        print("***********************************")
        print("     MODELO GRAMATICA REGULAR      ")
        print("***********************************")
        print("1.Crea gramatica regular")
        print("2.Cargar archivo de entrada")
        print("3.Evaluar cadenas")
        print("4.Eliminar recursividad por la izquierda")
        print("5.Guardar gramatica en archivo")
        print("6.Generar reporte gramatica regular")
        print("0.Regresar al menu principal")
        try:
            print("")
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            opcion = 8
        
        if opcion in range (0,7):
            if opcion == 1:
                crearGramatica()
            elif opcion == 2:
                cargarArchivoGramatica()
            elif opcion == 3:
                print("")
                print("En proceso :(")
                print("")
            elif opcion == 4:
                print("")
                print("En proceso :(")
                print("")
            elif opcion == 5:
                crearArchivoGramatica()
            elif opcion == 6:
                generarReporteGramatica()
            elif opcion == 0:
                menuPrincipal()
        else:
            print("")
            print("Opcion invalida, intente de nuevo :D")        
            print("")
