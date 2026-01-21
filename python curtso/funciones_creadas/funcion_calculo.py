def suma():
    num = input('decime un numero separado por "+" y lo sumo: ')
    numer = num.split("+")
    num= [int(x) for x in numer]
    return f'la suma de tus numeros es: {sum(num)}'
sumar_numeros = suma()

#cunado importes la funcion deves importar suma y num
#y poner print(suma(num)) pare que se pueda ver
# lo cambie ahora tambien solo puedes improtar sumar_numeros (from funcion_calculo import sumar_numeros)