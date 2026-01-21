#falto el profe y los pibes van a armar la clase

#pedir el nombre y la edad de los compañeros
def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input('ingrese su nombre: ')
        edad = int(input('ingrese su edad: '))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(4)

print(f'el prfesor es: {profesor} y el asistente: {asistente}')

