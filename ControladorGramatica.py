from Gramatica import Gramatica
from Producciones import Producciones
from graphviz import Digraph
import time
import os

listaNoTerminal = list()
listaGramatica = list()
listaTerminal = list()
listaProducciones = list()

def buscarNoTerminal(noTerminalUser):
    for noTerminal in listaNoTerminal:
        if noTerminal == noTerminalUser:
            return True
    return False


def buscarTerminal(terminalUser):
    for terminal in listaTerminal:
        if terminal == terminalUser:
            return True
    return False


def crearGramatica():
    noTerminal1 = ""
    terminales1 = ""
    noTerminalInicial = ""
    producciones1 = ""

    nombre = input("Escribe el nombre de la gramatica: ")

    while noTerminal1 != "fin":
        noTerminal1 = input("Escribe un no terminal: ")
        if buscarNoTerminal(noTerminal1) == False:
            if noTerminal1 == "fin":
                pass
            else:
                listaNoTerminal.append(noTerminal1)
        else:
            print("")
            print("El no terminal ya se encuentra en la lista :D") 
            print("") 


    while terminales1 != "fin":
        terminales1 = input("Escribe un terminal: ")
        if buscarTerminal(terminales1) == False and buscarNoTerminal(terminales1) == False:
            if terminales1 == "fin":
                pass
            else:
                listaTerminal.append(terminales1)
        else:
            print("")
            print("El terminal ya se encuentra en la lista y/o es un no terminal :D") 
            print("")


    while noTerminalInicial != "fin":
        noTerminalInicial = input("Escribe un no terminal Inicial: ")
        if buscarNoTerminal(noTerminalInicial) == True:
            noInicial = noTerminalInicial  
        else:
            if noTerminalInicial == "fin":
                continue
            else:     
                print("")
                print("El no terminal no se encuentra en la lista de no terminales.") 
                print("")    
    

    while producciones1 != "fin":
        try:
            producciones1 = input("Escribe las producciones: ").split(">")
            producciones2 = producciones1[1].split(" ")

            if (buscarNoTerminal(producciones1[0]) == True) and (buscarTerminal(producciones2[0]) == True) and (buscarNoTerminal(producciones2[1]) == True):
                listaProducciones.append(Producciones(producciones1[0],producciones2[0],producciones2[1]))
            else:
                print("Los terminales y/o no terminales no se encuentran, tienen que ser ingresadas antes :D")
        except IndexError:
            producciones1 == "fin"
            break  

    
    gramatica = Gramatica(nombre,listaNoTerminal,listaTerminal,noInicial,listaProducciones)
    listaGramatica.append(gramatica)
    print("")
    print("Gramatica agregada con exito! :D")
    print("")

def cargarArchivoGramatica():
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
                listaNoTerminal = file.split(",")
            if posicion == 3:
                file = file.rstrip('\n')
                listaTerminal = file.split(",")
            if posicion == 4:
                file = file.rstrip('\n')
                estadoNoInicial = file
            if posicion >= 5 and file != '%' and file != '%\n':
                file = file.rstrip('\n')
                produ = file.split(">")
                if produ[1] == "$":
                    lista_Temp.append(Producciones(str(produ[0]),str(produ[1]),str("")))
                else:
                    produ1 = produ[1].split(" ")
                    lista_Temp.append(Producciones(str(produ[0]),str(produ1[0]),str(produ1[1])))
            if file == '%' or file == '%\n':
                listaGramatica.append(Gramatica(nombre, listaNoTerminal, listaTerminal, estadoNoInicial, lista_Temp))
                lista_Temp = []
                posicion = 0
            posicion += 1

        print("Archivo cargado con exito! :D")

        # MUESTRA TODAS LAS GRAMATICAS
    y = 0
    for gram in listaGramatica:
        print("")
        print("*-----------------------------------------------")
        print("Nombre:", gram.nombre)
        print("No Terminales:", gram.noTerminal)
        print("Terminales: ", gram.terminales)
        print("No terminal Inicial: ", gram.noTerminalInicial)
        print("Producciones: ")
        for x in listaGramatica[y].producciones:
            print(str(x.inicio) + ">" + str(x.caracter) + " " + str(x.final))
        y += 1


def mostrarGramaticas():
    x=0
    for gram in listaGramatica:
        print(str(x) + "." + "" + gram.nombre)
        x +=1


def recorrerGramatica(solicitado):
    produccion1 = ""
    produccion2 = ""
    bandera = True
    inicial = listaGramatica[solicitado].noTerminalInicial
    for gram in listaGramatica[solicitado].noTerminal:
        if gram == inicial:
            for prod in listaGramatica[solicitado].producciones:
                if gram == prod.inicio:
                    if bandera == True:
                        produccion1 = produccion1 + gram + ">" + prod.caracter + " " + prod.final
                        bandera = False
                    else:
                        produccion1 = produccion1 + "\n" "  |" + prod.caracter + " " + prod.final
            bandera = True
        else:
            for prod in listaGramatica[solicitado].producciones:
                if gram == prod.inicio:
                    if bandera ==True:
                        produccion2 = produccion2 + gram + ">" + prod.caracter + " " + prod.final + "\n"
                        bandera = False
                    else:
                        produccion2 = produccion2 + "  |" + prod.caracter + " " + prod.final + "\n"
            bandera = True

    return produccion1 + "\n" + produccion2


def generarReporteGramatica():
    # y=0
    mostrarGramaticas()
    solicitado = int(input("Selecciona la gramatica para el reporte: "))

    dot = Digraph(name='dibujo', encoding='UTF-8', format='pdf')
    dot.attr(rankdir='LR', layout='dot', shape='circle')

    
    data = "Nombre: " + str(listaGramatica[solicitado].nombre) + '\n'
    data = data + 'No Terminal: ' + str(listaGramatica[solicitado].noTerminal) + '\n'
    data = data + 'Terminal: ' + str(listaGramatica[solicitado].terminales) + '\n'
    data = data + 'No Terminal inicial: ' + str(listaGramatica[solicitado].noTerminalInicial) + '\n'
    data = data + 'Producciones:' + '\n'
    data = data + str(recorrerGramatica(solicitado)) 
   
    
    dot.node(data, shape='component')

    # recorre la lista de estados
    for gram in listaGramatica[solicitado].noTerminal:
        # imprime todos los no terminales en nodos.
        dot.node(name=gram)


    dot.edge('Inicial', listaGramatica[solicitado].noTerminalInicial)
    # recorre todas las producciones
    for gram in listaGramatica[solicitado].producciones:
        # el simbolo $ significa estado de aceptacion, si en esa produccion
        # esta ese simbolo, el inicio de esa produccion se le dibuja un doble circulo
        if gram.caracter == "$":
            dot.node(name=gram.inicio, shape='doublecircle')
        else:
            # si no hay simbolo $, imprime los demas con circulos normales.
            dot.edge(str(gram.inicio), str(gram.final), label=gram.caracter)

    dot.render("ReporteGramatica"+str(solicitado), format='pdf', view=True)
    print("")
    print("Reporte generado con exito :D")
    print("")



def crearArchivoGramatica():
    encontrado = False
    for gram in listaGramatica:
        print(gram.nombre)
      
    nombre = input("Escribe el nombre de la Afd para generar el archivo: ")
    nombreArchivo = nombre + ".afd"
    y = 0
    for gram in listaGramatica:
        if gram.nombre == nombre:
            archivo = open(nombreArchivo, "w", encoding="utf-8")
            archivo.write(str(gram.nombre) + os.linesep)
            archivo.write(str(gram.noTerminal) + os.linesep)
            archivo.write(str(gram.terminales) + os.linesep)
            archivo.write(str(gram.noTerminalInicial) + os.linesep)
            archivo.write(str(recorrerGramatica(y)))
            archivo.close()
            encontrado = True
            print("")
            print("Gramatica encontrada y archivo generado con exito :D")
        y += 1
    
    if encontrado == False:
        print("")
        print("La gramatica que se escribió no existe :D")

