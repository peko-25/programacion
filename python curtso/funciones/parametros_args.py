
#forma no optima de sumar valores 
#def suma(lista):
#    numeros_sum = 0
#    for numero in lista:
#        numeros_sum = numeros_sum + numero
#    return numeros_sum
#resultado = suma([5,3,9,10,20,3])
#print(resultado)

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([5,3,9,10,20,3])
print(resultado2)

#lo de arriba pero utilizabndo el operador * como argumento (*args)
def suma_y_nombre(nombres,*numeros):
    return f'{nombres}, la suma de tus nomeros es: {sum(numeros)}'
resultado1 = suma_y_nombre('felipe',5,6,7,8,)
print(resultado1)

#forma que hice yo (feli) para contar valores y pedir nombre
num = input('decime un numero separado por " " y lo sumo: ')
numer = num.split(" ")
num= [int(x) for x in numer]
nombre = input('dime tu nombre: ')
print(type(nombre))

def suma(nombres,numeros):
    return f'{nombres}, la suma de tus nomeros es: {sum(numeros)}'
resultado = suma(nombre,num)
print(resultado)
