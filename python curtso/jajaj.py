import random
i=1
def generar_contraseña(longitud):
    caracteres = "abcdefghijklmñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ123456789"
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Solicitar al usuario la cantidad de dígitos
longitud_contraseña = int(input("Introduce la cantidad de dígitos de la contraseña: "))
for i in range(5): 
    print("--------------------------------------")
    contraseña = generar_contraseña(longitud_contraseña)
    print("Tu contraseña generada es:", contraseña)
    print 
    hola= dn