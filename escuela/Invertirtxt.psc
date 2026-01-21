Proceso Invertirtxt
    Definir txt Como Cadena
    Definir txt_invertido Como Cadena
    Definir i Como Entero
	
    // Solicitar al usuario que ingrese un txt
    Escribir "Ingrese un txt: "
    Leer txt
	long_txt<-Longitud(txt)
    txt_invertido <- ""
    Para i<-long_txt Hasta 1 con paso -1 Hacer 
		
        // Concatenar cada carácter en orden inverso
        txt_invertido <- Concatenar(txt_invertido, Subcadena(txt, i, i))
		Escribir i
    FinPara
	
    // Mostrar el txt invertido
    Escribir "txt invertido: " txt_invertido
FinProceso
