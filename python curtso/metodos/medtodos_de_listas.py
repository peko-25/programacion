lista = list([15, 12, 1])

print(lista)
cadena = "hola"
resultado = len(lista)#devuelve la cantidad de la lista

lista.append(55)#agregar un elemento a las lista

#agregar un elemento a la lista en un indice especifico
lista.insert(2, "toma pelotudo")

#agrega varios elementos a la lista
lista.extend([False, 2023, 2])

#eliminando un elemento por el indice
lista.pop(-1)#-1 para eliminar el ultimo -2 el ante ultimo y sigue

lista.remove("toma pelotudo")
#lista.clear()

#ordenando la lista si usamos reverse=true ordena inverso
lista.sort()

lista.reverse()

print(lista)
