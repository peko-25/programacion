Algoritmo cant_mayus_mins
	Escribir "escriba un texto"
	leer txt
	long_txt<-Longitud(txt)
	cont_mayus<-0
	cont_mins<-0
	para i<-1 Hasta long_txt Con Paso 1 Hacer
		sub_txt<-Subcadena(txt,i,i)
		Segun sub_txt Hacer
			" ":
			
			Mayusculas(sub_txt):
				cont_mayus<- cont_mayus+1
			minusculas(sub_txt):
				cont_mins<-cont_mins+1
			De Otro Modo:
				
		Fin Segun
	FinPara
	Escribir "la cantidad de mayusculas es " cont_mayus " y la cantidad de minusculas es " cont_mins
	
FinAlgoritmo
