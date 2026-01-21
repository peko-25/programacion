Proceso GenerarContraseña
    Definir long Como Entero
    Definir caractere Como Cadena
    Definir contraseña Como Cadena
    Definir i Como Entero
    Definir posicion Como Entero
    // Definir los caracteres permitidos
    caractere <- "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-.,*"
    // Solicitar la longitud de la contraseña
    Escribir "Ingrese la longitud de la contraseña: "
    Leer long
	
    // Inicializar la contraseña
    contraseña <- ""
    // Generar la contraseña
    Para i <- 1 Hasta long Hacer
        // Generar una posición aleatoria
        posicion <- Aleatorio(1, Longitud(caractere))
        // Concatenar el carácter seleccionado
		sub_carc<-Subcadena(caractere, posicion, posicion)
        contraseña <- Concatenar(contraseña,sub_carc)
		Escribir "----------"
		Escribir contraseña
		Escribir "----------"
    FinPara

	
    // Mostrar la contraseña generada
    Escribir "Contraseña generada: ", contraseña
FinProceso
