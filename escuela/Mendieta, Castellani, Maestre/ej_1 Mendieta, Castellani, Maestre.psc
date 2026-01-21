Funcion invercion <- inverso ( pal,long )
	long<-Longitud(pal)
	para i<-long Hasta 1 Con Paso -1 Hacer
		sub<-SubCadena(pal, i, i)
		invertido<-Concatenar(invertido,sub)
	FinPara
	invercion<-invertido
Fin Funcion



Algoritmo ej_1
	Definir pal Como Caracter
	definir long Como Entero
	Escribir "escriba una palabra"
	leer pal
	long<-longitud(pal)
Escribir inverso(pal,long)
FinAlgoritmo
