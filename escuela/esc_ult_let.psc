Algoritmo esc_ult_let
	Escribir "escriba un texto"
	leer txt
	cant_l_txt<-Longitud(txt)
	a<-0
	Repetir
	a<-a+1
	
	rn<-Aleatorio(1,cant_l_txt)
	Escribir rn
	para i<-1 Con Paso 1 Hasta cant_l_txt hacer
		texf<-Subcadena(txt,i,i)
		si i=rn Entonces
			texff<-texf
			
		FinSi
	FinPara
	Escribir "--------------------" 
	Escribir a
	Escribir "--------------------oo"
	Escribir texff
	Escribir "--------------------ooo"
Hasta Que rn=cant_l_txt
FinAlgoritmo
