from Afd import Afd
from Transiciones import Transiciones
import time
import os
from graphviz import Digraph


listaAfd = list()
listaEstado = list()
listaAlfabeto = list()
listaAceptacion = list()
listaTransiciones = list()
salida = False


def limpiarArreglos():
    listaEstado.clear()
    listaAlfabeto.clear()
    listaAceptacion.clear()
    listaTransiciones.clear()


def buscarEstado(listaEstado,palabra):
    for estado in listaEstado:
        if estado == palabra:
            return True
        else:
            pass      
    return False


def buscarAfd(listaAfd, palabra):
    for afd in listaAfd:
        if afd.nombre == palabra:
            return True    
        else:
            pass
    return False


def buscarAlfabeto(listaAlfabeto,palabra):
    for alfa in listaAlfabeto:
        if alfa == palabra:
            return True
        else:
            pass
    return False


def buscarSimboloTransicion(lista, simbolo):
    for trans in listaTransiciones:
        if trans.caracter == simbolo:
            return True
        else:
            pass
    return False


def crearAFD():
    alfabeto1 = ""
    aceptacion1 = ""
    transiciones1 = ""
    print("")
    nombre = input("Escribe el nombre de la automata: ")
    print("")
    print("Escribe 'fin' para terminar de escribir los estados, alfabetos y aceptacion.")
    estado = input("Escribe los estados: ")
    listaEstado.append(estado)
    for estado in listaEstado:
        estado = input("Escribe los estados: ")
        if estado == "fin":
            break
        else:
            listaEstado.append(estado)


    while alfabeto1 != "fin":
        alfabeto1 = input("Ingrese los alfabetos: ")
        if buscarEstado(listaEstado,alfabeto1) == True:
            print("")
            print("No se pueden llamar alfabetos iguales que los estados :D")
            print("Regresando a crear la automata....")
            limpiarArreglos()
            time.sleep(2)
            crearAFD()
            break
        if buscarAlfabeto(listaAlfabeto,alfabeto1) == True:
            print("")
            print("No se pueden ingresar alfabetos iguales :D")
            print("Regresando a crear la automata....")
            limpiarArreglos()
            time.sleep(2)
            crearAFD()
            break
        else:
            if alfabeto1 == "fin":
                pass
            else:
                listaAlfabeto.append(alfabeto1)
            

    inicial = input("Escribe el estado inicial: ")
    if buscarEstado(listaEstado,inicial) == True:
        pass
    else:
        print("")
        print("El estado ingresado no se encuentra en la lista de estados :D")
        print("Regresando a crear la automata....")
        limpiarArreglos()            
        time.sleep(2)
        crearAFD()


    while aceptacion1 != "fin":
        aceptacion1 = input("Escribe los estados de aceptacion: ")
        if buscarEstado(listaEstado,aceptacion1) == True:
            listaAceptacion.append(aceptacion1)
        else:
            if aceptacion1 == "fin":
                break
            else:
                print("")
                print("El estado ingresado no se encuentra en la lista de estados :D")
                print("Regresando a crear la automata....")
                limpiarArreglos()            
                time.sleep(2)
                crearAFD()        

    
    while transiciones1 != "fin":
        transiciones1 = input("Escribe tu transicion: ").split(",")
        if (buscarEstado(listaEstado,str(transiciones1[0])) == True) and (buscarAlfabeto(listaAlfabeto,str(transiciones1[1])) == True) and (buscarEstado(listaEstado,str(transiciones1[2])) == True): 
            trans = Transiciones(str(transiciones1[0]),str(transiciones1[1]),str(transiciones1[2]))
            listaTransiciones.append(trans)
        else:    
            if str(transiciones1[0]) == "fin":
                break
            else:
                print("")
                print("Alguno de tus estados/alfabetos no se encuentran en la lista :D")
                print("Regresando a crear la automata....")
                limpiarArreglos()            
                time.sleep(2)
                crearAFD()    

    listaAfd.append(Afd(nombre,listaEstado,listaAlfabeto,inicial,listaAceptacion,listaTransiciones))
    print("")
    print("AFD creado con exito! :D")
    
    y = 0
    for afd in listaAfd:
        print("")
        print("*-----------------------------------------------")
        print("Nombre: ", afd.nombre)
        print("Estados: ", afd.estados)
        print("Alfabeto: ", afd.alfabeto)
        print("Estado Inicial: ", afd.estadoInicial)
        print("Estado Aceptacion: ", afd.estadoAceptacion)
        print("Transiciones: ")
        for x in listaAfd[y].transiciones:
            print("" + str(x.inicio) + "," + str(x.caracter) + ";" + str(x.final))
        y += 1
  

def cargarArchivo():
    ruta = input("Escribe el nombre del archivo: ")
    with open(ruta, "r") as file:
        posicion = 1
        line = file.readlines()
        lista_Temp = []
        for file in line:
            file.rstrip('\n')
            if posicion == 1:
                file = file.rstrip('\n')
                nombre = file
            if posicion == 2:
                file = file.rstrip('\n')
                listaEstado = file.split(",")
            if posicion == 3:
                file = file.rstrip('\n')
                listaAlfabeto = file.split(",")
            if posicion == 4:
                file = file.rstrip('\n')
                estadoInicial = file
            if posicion == 5:
                file = file.rstrip('\n')
                listaAceptacion = file.split(",")
            if posicion >= 6 and file != '%' and file != '%\n':
                file = file.rstrip('\n')
                trans = file.split(',')
                trans1 = trans[1].split(';')
                lista_Temp.append(Transiciones(str(trans[0]),str(trans1[0]),str(trans1[1])))
            if file == '%' or file == '%\n':
                listaAfd.append(Afd(nombre, listaEstado, listaAlfabeto, estadoInicial, listaAceptacion, lista_Temp))
                lista_Temp = []
                posicion = 0
            posicion += 1

        print("Archivo cargado con exito! :D")
    
    
    # MUESTRA TODAS LAS AFD
    y = 0
    for afd in listaAfd:
        print("")
        print("*-----------------------------------------------")
        print("Nombre: ", afd.nombre)
        print("Estados: ", afd.estados)
        print("Alfabeto: ", afd.alfabeto)
        print("Estado Inicial: ", afd.estadoInicial)
        print("Estado Aceptacion: ", afd.estadoAceptacion)
        print("Transiciones: ")
        for x in listaAfd[y].transiciones:
            print("" + str(x.inicio) + "," + str(x.caracter) + ";" + str(x.final))
        y += 1



def guardarArchivoAFD():
    nombreAfd = input("Escribe el nombre de la Afd para generar el archivo: ")
    nombreArchivo = nombreAfd + ".afd"
    encontrado = False
    
    i=0
    for item in listaAfd:
        if item.nombre == nombreAfd:    
            archivo = open(nombreArchivo, "w", encoding="utf-8")
            archivo.write(str(item.nombre) + os.linesep)
            archivo.write(str(item.estados) + os.linesep)
            archivo.write(str(item.alfabeto) + os.linesep)
            archivo.write(str(item.estadoInicial) + os.linesep)
            archivo.write(str(item.estadoAceptacion) + os.linesep)
            for trans in listaAfd[i].transiciones:
                archivo.write(str(trans.inicio) + "," + str(trans.caracter) + ";" + str(trans.final) + os.linesep)
            archivo.close()
            encontrado = True
            print("")
            print("Automata encontrado y archivo generado con exito :D")
        i += 1

    if encontrado == False:
        print("")
        print("La automata ingresada no se encuentra en la lista :D")
    else:
        pass



def mostrarAfd():
    print("*********************")
    print("   LISTA DE AFD'S    ")
    print("*********************")
    i=0
    for x in listaAfd:
        print(str(i) + "." +  x.nombre)
        i += 1    
    print("") 



def recorrerGramatica(solicitado):
    produccion1 = ""
    produccion2 = ""
    bandera = True
    inicial = listaAfd[solicitado].estadoInicial
    for afd in listaAfd[solicitado].estados:
        if afd == inicial:
            for trans in listaAfd[solicitado].transiciones:
                if afd == trans.inicio:
                    if bandera == True:
                        produccion1 = produccion1 + afd + ">" + trans.caracter + " " + trans.final
                        bandera = False
                    else:
                        produccion1 = produccion1 + "\n" "  |" + trans.caracter + " " + trans.final
            bandera = True
        else:
            for trans in listaAfd[solicitado].transiciones:
                if afd == trans.inicio:
                    if bandera ==True:
                        produccion2 = produccion2 + afd + ">" + trans.caracter + " " + trans.final + "\n"
                        bandera = False
                    else:
                        produccion2 = produccion2 + "  |" + trans.caracter + " " + trans.final + "\n"
            bandera = True

    return produccion1 + "\n" + produccion2


def buscarEstadoAceptacion(solicitud, posicion):
    for x in listaAfd[posicion].estadoAceptacion:
        if x == solicitud:
            return True
    return False


def evaluarCadena():
    mostrarAfd()
    selecciona = int(input("Selecciona la automata para evaluar una cadena:"))
    cadena = input("Ingrese la cadena: ")


    estadoI = listaAfd[selecciona].estadoInicial
    for x in cadena:
        for afd in listaAfd[selecciona].transiciones:
            if afd.inicio == estadoI:
                if x == afd.caracter:
                    estadoI = afd.final
                    # error F :c
                    # print(str(estadoI))
    
    if buscarEstadoAceptacion(estadoI,selecciona) == True:
        # print(str(estadoI))
        print("La cadena es valida :D") 
    else:
        # print(str(estadoI))
        print("La cadena no es valida :D")
    
    # for x in cadena:
    #     for afd in listaAfd[selecciona].transiciones:
    #         if afd.inicio == listaAfd[selecciona].estadoInicial:
    #             if x == afd.caracter:
    #                 bandera == True
    #     if listaAfd[selecciona].estadoInicial == listaAfd[selecciona].estadoAceptacion:
    #         bandera = True
    #         return bandera      
    #     else:
    #         bandera = False 
    #         return bandera
    


    # if bandera == True:
    #     print("La cadena es valida.")
    # else: 
    #     print("La cadena no es valida.")


def generarReporte():
    mostrarAfd()
    solicitado = int(input("Selecciona la automata para el reporte: "))
   
    # crear archivo
    dot = Digraph(name='dibujo', encoding='UTF-8', format='pdf')
    dot.attr(rankdir='LR', layout='dot', shape='circle')

    
    data = "Nombre: " + str(listaAfd[solicitado].nombre) + '\n'
    data = data + 'Estados: ' + str(listaAfd[solicitado].estados) + '\n'
    data = data + 'Estado inicial: ' + str(listaAfd[solicitado].estadoInicial) + '\n'
    data = data + 'Estado aceptacion: ' + str(listaAfd[solicitado].estadoAceptacion) + '\n'
    data = data + 'Transiciones:' + '\n'
    
    for afd in listaAfd[solicitado].transiciones:
        data = data + str(afd.inicio) + "," + str(afd.caracter) + ";" + str(afd.final) + '\n'

    # crear nodos
    dot.node(data, shape='component')

    # recorre la lista de estados
    for afd in listaAfd[solicitado].estados:
        # revisa si los estados de aceptacion se encuentran en los estados para doble circulo
        if afd in listaAfd[solicitado].estadoAceptacion:
            dot.node(name=afd, shape='doublecircle')
        else:
            dot.node(name=afd)
    
    dot.edge('Inicial', listaAfd[solicitado].estadoInicial)
    for afd in listaAfd[solicitado].transiciones:
        # unir nodos!
        dot.edge(str(afd.inicio), str(afd.final), label=afd.caracter)


    dot.render("ReporteAFD"+str(solicitado), format='pdf', view=True)
    print("")
    print("Reporte generado con exito :D")
    print("")


def generarGramatica():
    mostrarAfd()
    solicitado = int(input("Escribe la automata para la gramatica: "))
    print("")
    print("------------------------------------------------------")
    print("Terminales: ", str(listaAfd[solicitado].alfabeto))
    print("No terminales: ",  str(listaAfd[solicitado].estados))
    print("Inicio: ", str(listaAfd[solicitado].estadoInicial))
    print("Producciones:")
    print(recorrerGramatica(solicitado))
    print("")
    pregunta = input("Escribe 'si', si quieres generar el archivo o 'no' para continuar...")

    if pregunta == "si":
        archivo = open("GramaticaRegular.txt", "w", encoding="utf-8")
        archivo.write(str(listaAfd[solicitado].nombre) + os.linesep)
        archivo.write(str(listaAfd[solicitado].estados) + os.linesep)
        archivo.write(str(listaAfd[solicitado].alfabeto) + os.linesep)
        archivo.write(str(listaAfd[solicitado].estadoInicial) + os.linesep)
        archivo.write(str(recorrerGramatica(solicitado)))
        archivo.close()
        print("")
        print("Archivo generado con exito :D")
        time.sleep(3)
        print("")
        pregunta2 = input("Quieres limpiar la consola?: ")
        if pregunta2 == "si":
            os.system("cls")
        else:
            pass
    else:
        pass
    


    
    
