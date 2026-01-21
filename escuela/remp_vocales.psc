Algoritmo remp_vocales
	Definir le Como Caracter
	Escribir "escriba un texto"
	leer txt
	cant_l_txt<-Longitud(txt)
	para i<-1 Con Paso 1 Hasta cant_l_txt Hacer
		le<-Subcadena(txt,i,i)
		Segun le Hacer
			"a":
				palf<-Concatenar(palf,"@")
			"o":
				palf<-Concatenar(palf,"@")
			De Otro Modo:
				palf<-Concatenar(palf,le)
		Fin Segun
	FinPara
	Escribir palf
FinAlgoritmo

