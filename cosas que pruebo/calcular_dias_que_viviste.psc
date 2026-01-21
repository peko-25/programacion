Algoritmo calcular_dias_que_viviste
	Definir ANO_NACIMIENTO, mes_nacimiento, dia_nacimiento Como Entero
	Definir ANO_ACTUAL, mes_actual, dia_actual Como Entero
	Definir dias_nacimiento, dias_actual, dias_que_viviste Como Entero
	Escribir 'Ingresa tu año de nacimiento: '
	Leer ANO_NACIMIENTO
	Escribir 'Ingresa tu mes de nacimiento: '
	Leer mes_nacimiento
	Escribir 'Ingresa tu día de nacimiento: '
	Leer dia_nacimiento
	ANO_ACTUAL <- 2024
	mes_actual <- 03
	dia_actual <- 24
	dias_nacimiento <- ANO_NACIMIENTO*365+mes_nacimiento*30+dia_nacimiento
	dias_actual <- ANO_ACTUAL*365+mes_actual*30+dia_actual
	dias_que_viviste <- dias_actual-dias_nacimiento
	Escribir 'Has vivido ', dias_que_viviste, ' días'
FinAlgoritmo
