from datetime import datetime

def calcular_dias_que_viviste(fecha_nacimiento):
    fecha_actual = datetime.now()
    
    diferencia = fecha_actual - fecha_nacimiento
    
    dias_que_viviste = diferencia.days
    
    return dias_que_viviste

fecha_nacimiento = datetime.strptime(input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): "), "%d/%m/%Y")

dias_que_viviste = calcular_dias_que_viviste(fecha_nacimiento)
print(f"Has vivido {dias_que_viviste} dias")
