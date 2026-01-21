Proceso QuitarRepetidos
    Definir txt Como Cadena
    Definir resultado Como Cadena
    Definir i Como Entero
	
    // Solicitar el txt al usuario
    Escribir "Ingrese un txt: "
    Leer txt
	long_txt<-Longitud(txt)
    // Inicializar la variable de resultado
    resultado <- ""
    // Recorrer el txt
    Para i <- 1 Hasta long_txt Hacer
		sub_resl<-Subcadena(resultado,Longitud(resultado),i)
		sub_txt<-Subcadena(txt, i, i)
        Si resultado = "" O sub_resl <> Sub_txt Entonces
            resultado <- Concatenar(resultado, Sub_txt)
        FinSi
		Escribir resultado "----"
    FinPara
    // Mostrar el resultado
    Escribir "Resultado: ", resultado
FinProceso
