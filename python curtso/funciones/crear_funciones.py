
#creando una funcion simple
#def saludar():
#    print('hola dalto,mi maestro ¿como estas?')

#ejecutando funcion simple
#saludar()

#crear funcion que tenga parametros
#def saludar(nombre,sexo):
    #nombre = input("dime tu nombre: ")
    #sexo = input("dime tu sexo: ")
#    sexo = sexo.lower()
#    if (sexo == 'mujer'):
#        adjetivo = "reina"
#    elif (sexo == "hombre"):
#        adjetivo = 'loco'
#    else:
#        adjetivo = 'no lo sabemos'
    
#    print(f'hola {nombre}, {adjetivo} como estas')
    
#saludar(nombre,sexo)

#creando una funcion que retorne valores

def contra_random():
    num = (input("dime un numero: "))
    chars = "abcdefghijlkjblhblkjaerfg"
    num_entero = str(num)
    print(num_entero)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
#desepaquetando la funcion mostrando el reslultado del mcontenido y los datos para crearlo
password,primer_numero = contra_random()
print(f"tu contraseña nueva es: {password}")
print(f"para crearla utilizaste el numero: {primer_numero}")
