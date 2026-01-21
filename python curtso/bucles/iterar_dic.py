dicionario = {
    'nombre' : "feli",
    'apellido' : "mendieta",
    'flotante' : 1.85
}

#recorriendo diccionario para optener las key y el valor
for key,value in dicionario.items():
    print(f'la clave es: {key} y el valor es: {value}')
    
#recorriendo diccionario para optener las key 
for key in dicionario:
    print(f'la clave es: {key}')