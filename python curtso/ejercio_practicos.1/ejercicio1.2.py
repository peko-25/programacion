pedir_palabra = input('decime unas plabras y tedigo cuanto tardas en decirlo: ')
separar_palabrtas = pedir_palabra.split(" ")
cantidad_de_palabras= len(separar_palabrtas)
print(cantidad_de_palabras)


#print(f"dijiste3 {cantidad_de_palabras} en {cantidad_de_palabras /2 } segundos")
#print(f"dalto lo diria en {cantidad_de_palabras /2 *1.3 } segundos")

if cantidad_de_palabras < 120:
    print(f"dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras /2 } segundos en decirlo")
    print(f"dalto lo diria en {cantidad_de_palabras *100 //2 *1.3 /100 } segundos")
else:
    print("flaco te pedi unas palabras no un testamento")