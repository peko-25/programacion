numero = [1,2,3,4,5,6,7,8,9,12,10,13,14]

#creando funcion lambda mara multiplicando por 2
multiplicar_por_dos= lambda x : x*2

#creando funcion comun que diga si es par o no
#def es_par(num):
#    if (num%2==1):
#        return True
#usando filter con una funcion comun
#numeros_pares = filter(es_par,numero)


#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero:numero%2==0,numero)
print(list(numeros_pares))
