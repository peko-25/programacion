ingreso_mensual = 100000
gasto_mensual = 100000

#if anidados
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual <0:
        print('estas en la mierda')
    elif ingreso_mensual - gasto_mensual > 3000:
        print('estas re piola')
    else:
        print('gastas mucha money bro')
        print("estas bien en cualquier parte del mundo")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
    
elif ingreso_mensual > 400:
    print("estas bien en arg")

else:
    print("sos pobre")