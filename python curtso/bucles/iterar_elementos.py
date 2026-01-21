animales = ["perro","gato","loro","cocodrilo",'pez']
numeros = [31,21,12,23,14]

#recorriendo la lista animales
for animal in animales:
    print(f'ahora la variable animal es igual {animal}')
    
#recorriendo la lista numeros y multiplicando cada valor por 2
for numero in numeros:
    resltado = numero*2
    print(resltado)
    
    
#interarando dos listas del mismo tamoño al mismo tiempo
for numero,animal in zip(numeros,animales):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')


#forma no optima de rocorrer lista con su indice (no funciona para conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
    
#forma correcta de recorrer lista con su indice
for i,num in enumerate(numeros):
    print(f'el indice es {i} y el valor es {num}')
    




#usando el for / else
for numer in numeros:
    print(f'ejecutando el ultimo blucle, valor actual: {numer}%')

else:
    print('el bucle termino')
    
#todo lo anterior sirve igual para tuplas y conjuntos
