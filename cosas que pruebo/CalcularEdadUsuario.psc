Algoritmo CalcularEdadUsuario
	Definir fechaNacimientoTexto, diaNacimientoTexto, mesNacimientoTexto, anoNacimientoTexto Como Cadena
	Definir diaNacimiento, mesNacimiento, anoNacimiento Como Entero
	Definir edad Como Entero
	Definir edadTexto Como Cadena
	
	Escribir "Ingrese su fecha de nacimiento (dd/mm/aaaa): "
	Leer fechaNacimientoTexto
	
	diaNacimientoTexto <- SubCadena(fechaNacimientoTexto, 1, 2)
	mesNacimientoTexto <- SubCadena(fechaNacimientoTexto, 4, 5)
	añoNacimientoTexto <- SubCadena(fechaNacimientoTexto, 7, 10)
	
	diaNacimiento <- ConvertirANumero(diaNacimientoTexto)
	mesNacimiento <- ConvertirANumero(mesNacimientoTexto)
	añoNacimiento <- ConvertirANumero(anoNacimientoTexto)
	
	Definir diaActual, mesActual, añoActual Como Entero
	edad <- 0
	diaActual <- 25
	mesActual <- 3
	añoActual <- 2024
	Si (mesActual < mesNacimiento) O ((mesActual == mesNacimiento) Y (diaActual < diaNacimiento)) Entonces
		edad <- añoActual - añoNacimiento - 1
	SiNo
		edad <- añoActual - añoNacimiento
	FinSi
	
	edadTexto <- Concatenar("Su edad es: ", ConvertirATexto(edad))
	edadTexto <- Concatenar(edadTexto, " años.")

	Escribir edadTexto
FinAlgoritmo
