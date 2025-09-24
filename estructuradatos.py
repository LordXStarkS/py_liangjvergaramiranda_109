# # estructura de datos dinamicas
# # listas, tuplas, diccionarios, conjuntos
# #
# #listas = [2,1,4,5,6,7,8,9, "hola", true, 3.5]
# #tuplas = (2,1,4,5,6,7,8,9)
# #conjuntos = {2,1,4,5,6,7,8,9}

# estructuraLista = [2,1,4,5,8,8,5,4,7,1,5,8,7,9]
# cantidadDatos = estructuraLista.__len__()

# i = 0
# while(i <= cantidadDatos - 1):
#     print(estructuraLista[i])
#     i = i + 1

# for item in estructuraLista:
#     print(item)

# #diccionarios = {"nombre":"geostark", "edad": 34, "nacionalidad" : "peruano"}

# print("el valor maximo de la estructura es: ", max(estructuraLista) )
# print("el valor minimo de la estructura es: ", min(estructuraLista) )
# print("el valor promedio de la estructura es: ", sum(estructuraLista) / cantidadDatos )
# print("la cantidad de elementos de la estructura es: ", cantidadDatos )

# # #lista
# # #tupla
# # numeros = [140,20,90,40,50,95,100]

# # numeros.append(95)
# # numeros.append(100)
# # numeros.append(180)

# # cantidadDatos = numeros.__len__()
# # print(cantidadDatos)
# # print(numeros)
# # ultimo = numeros.pop()
# # #print(ultimo)

# # numeros.sort()
# # #print(numeros)

# # indice = 0

# # while(indice <= cantidadDatos - 1):
# #     print(numeros[indice])
# #     indice = indice + 1

# # #numeros.remove(20)

# #tuplas
# colores = ("azul", "rojo", "amarillo", "azul", "verde", "rojo", "rojo")

# # #cantidad de elementos que se repiten
# # valoresRepetidos = colores.count("azul")
# # indice = colores.index("rojo")
# # print(indice)

# # print(valoresRepetidos)

# for color in colores:
#     print(color)


# #conjuntos
# conjuntoA = {1,2,3,6,5,4,9,9,8,7,1,2,3}

# conjuntoB = {2,3,16,19,18}

# #for elemento in conjuntos:
# #    print(elemento)

# #print(conjuntoA.union(conjuntoB))
# #print(conjuntoA.intersection(conjuntoB))
# #print(conjuntoA.difference(conjuntoB))

# estructuraLista = [2,1,4,5,8,8,5,4,7,1,5,8,7,9]
# conjunto = set(estructuraLista)
# print(conjunto)

# productos = ["manzanas", "leche", "pan", "leche", "pan", "peras"]

# productos_unicos = set(productos)
# print (productos_unicos)



#======================diccionarios========================

#key
#value

persona1 = {
                "nombre":"geostark",
                "edad": 34,
                "nacionalidad" : "peruano"}

persona2 = {
                "nombre":"rocio",
                "edad": 36,
                "nacionalidad" : "peruano"}

persona3 = {
                "nombre":"karim",
                "edad": 38,
                "nacionalidad" : "peruano"}

persona1["nombre"] = "Liang"

print(persona1["nombre"])
persona1.pop("edad")
persona1.update({"fechaNacimiento": "07-03-1991"})

print(persona1)
