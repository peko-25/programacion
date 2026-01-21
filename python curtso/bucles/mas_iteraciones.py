#creando las litas
frutas = ["Manzana", "banana", "Naranja", "Uva", "frutilla", "Piña", "Mango"]
cadena = "hola felipe"
numeros =[2,5,8,10]
#evitando que sea Uva con continue
for fruta in frutas:
    if fruta == "Uva":
        continue
    print(f'la frutas es: {fruta}')
    
print("--------------------------")

#evitando que el bucle siga (el else tmp se ejecuta)
for fruta in frutas:
    print(f'la frutas es: {fruta}')
    if fruta == "Uva":
        break
else:
    print('bucle terminado')
    
print("--------------------------")
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
print("--------------------------")
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicado= [x*2 for x in numeros]
print(numeros_duplicado)
