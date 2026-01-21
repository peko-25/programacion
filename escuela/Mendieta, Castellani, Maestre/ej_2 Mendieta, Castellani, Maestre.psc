Funcion resultado<-codificar(tex)
	long = longitud(tex)
	Para i<-1 Hasta long Con Paso 1 
		sub<-Subcadena(tex,i,i)
		sub<-Minusculas(sub)
		Si sub="a" O sub ="c" Entonces
			resultado<-Concatenar(resultado,"*")
		SiNo
			resultado<-Concatenar(resultado,sub)
		FinSi
	FinPara
	
FinFuncion
Funcion r <- ocultar ( c )
	Definir long Como Entero
	Definir r Como Caracter
	long = longitud(c)
	r<-Subcadena(c, 1, long - 4) + "****"
	
Fin Funcion
Algoritmo ocultar_contraseña
	Definir respuesta,A Como Caracter
	Escribir "ingresar contraseña"
	leer A
	respuesta<-codificar(A)
	respuesta<-ocultar(respuesta)
	Escribir respuesta
FinAlgoritmo
