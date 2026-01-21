#creando una funcion de 3 parametrod

#def frase(nombre,apellido,adjetivo):
#    return f'hola {nombre} {apellido}, sos muy {adjetivo}'

#utilizando keyword argumens
#frase_resultante = frase(adjetivo='capo',nombre='feli',apellido='mendi')


#creando la misma funcion con un parametro opcional y valor por defecto
def frase(nombre,apellido,adjetivo= 'capo'):
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase('feli','mendi','inteligente')
print(frase_resultante)

