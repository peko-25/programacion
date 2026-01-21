def calcular_tiempo_y_dias(puntos_deseados, nivel_2=False):
    # Puntos y tiempos por día
    puntos_pc_nivel_1 = 105
    puntos_pc_nivel_2 = 105 + 150  # Nivel 2 añade 150 puntos extra
    tiempo_pc_min = 8  # Tiempo mínimo en PC
    tiempo_pc_max = 10  # Tiempo máximo en PC
    puntos_movil = 90
    tiempo_movil = 2  # Tiempo en móvil en minutos
    puntos_racha = 45  # Puntos adicionales cada 3 días

    # Puntos y tiempos totales por día
    if nivel_2:
        puntos_por_dia_pc = puntos_pc_nivel_2
    else:
        puntos_por_dia_pc = puntos_pc_nivel_1
    
    puntos_por_dia_total = puntos_por_dia_pc + puntos_movil
    tiempo_por_dia_pc = (tiempo_pc_min + tiempo_pc_max) / 2  # Promedio de tiempo en PC
    tiempo_por_dia_total = tiempo_por_dia_pc + tiempo_movil  # Tiempo total diario

    # Calcular días y puntos adicionales por racha de 3 días
    dias_necesarios = 0
    puntos_acumulados = 0
    while puntos_acumulados < puntos_deseados:
        dias_necesarios += 1
        puntos_acumulados += puntos_por_dia_total
        
        # Cada 3 días, sumar los puntos de racha
        if dias_necesarios % 3 == 0:
            puntos_acumulados += puntos_racha

    # Volver a calcular el número de días necesarios si sobrepasa la cantidad de puntos deseada
    puntos_excedentes = puntos_acumulados - puntos_deseados

    # Si los puntos acumulados exceden los puntos deseados, ajustar los días
    if puntos_excedentes > 0:
        dias_necesarios -= 1  # Ajustar si es necesario

    # Calcular tiempo total
    tiempo_total_minutos = dias_necesarios * tiempo_por_dia_total
    tiempo_total_horas = tiempo_total_minutos / 60

    # Resultados
    print(f"Días necesarios: {dias_necesarios}")
    print(f"Tiempo total estimado: {tiempo_total_minutos:.2f} minutos ({tiempo_total_horas:.2f} horas)")

# Ejemplo de uso
puntos_deseados = int(input("Ingresa la cantidad de puntos que deseas conseguir: "))
nivel_2 = input("¿Tienes nivel 2 en Microsoft Rewards? (si/no): ").lower() == "si"

calcular_tiempo_y_dias(puntos_deseados, nivel_2)
