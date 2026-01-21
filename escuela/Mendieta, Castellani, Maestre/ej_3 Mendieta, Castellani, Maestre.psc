Funcion r <- cont_esp ( txt )
	long<-Longitud(txt)
	cant_esp<-0
	para i<-1 Hasta long hacer 
		sub<-Subcadena(txt,i,i)
		si sub=" " Entonces
			cant_esp<-cant_esp+1
		FinSi
	FinPara
	si cant_esp>5 Entonces
		Escribir "el texto es espacioso"
	SiNo
		Escribir "el texto es comprimido"
	FinSi
Fin Funcion
Algoritmo contar_espacios
	Definir tex,resp Como Caracter
	Escribir "escriba un texto"
	leer tex
	resp<-cont_esp(tex)
	Escribir resp
	
FinAlgoritmo
