Algoritmo cont_vocales
	Definir le Como Caracter
	Escribir "escriba un texto"
	leer txt
	txt<-Minusculas(txt)
	cant_l_txt<-Longitud(txt)
	cant_voc<-0
	para i<-1 Con Paso 1 Hasta cant_l_txt Hacer
		le<-Subcadena(txt,i,i)
		Segun le Hacer
			"a":
				cant_voc<-cant_voc+1
			"e":
				cant_voc<-cant_voc+1
			"i":
				cant_voc<-cant_voc+1
			"o":
				cant_voc<-cant_voc+1
			"u":
				cant_voc<-cant_voc+1
			De Otro Modo:
				
		Fin Segun
	FinPara
	Escribir cant_voc
FinAlgoritmo
