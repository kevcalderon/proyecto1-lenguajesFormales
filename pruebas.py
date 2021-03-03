# separar las transiciones e ingresarlas al objeto transiciones

inicio = input("Ingrese las transiciones: ").split(",")
if str(inicio[0]) == "fin":
    print("se termino :v")
else:
    print(str(inicio[0]) + " " + str(inicio[1]) + " " + str(inicio[2]))

# unir dos strings

nombre = "archivo"
ruta = nombre + '.afd'
print(ruta)