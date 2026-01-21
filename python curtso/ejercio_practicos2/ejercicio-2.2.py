#crando una funcion que devuelva numeros primos 
#entre el 0 y el argumento que pasamos

#creando funcion que verifique que numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse
    #por ningun numero entre dos y ese mismo -1
    for i in range(2,num-1):
        if num % i ==0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo 
    return True

#creando una funcion  que retorne una lista con todos los primos
hola = int(input("dime un numero y te dire los cuantos primos hay del 0 al numero: "))
def primos_hasta(num):
    #creando lista
    primos = []
    for i in range(3,num + 1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(hola)
print(resultado)