Algoritmo nickname1
	Escribir "escriba su nombre"
	leer nom
	Escribir "escriba su apellido"
	leer ape
	subnom<-Subcadena(nom,1,3)
	longape<-Longitud(ape)
	ul3ape<-longape-2
	subape<-Subcadena(ape,ul3ape,longape)
	nickname<-Concatenar(subnom,subape)
	Escribir nickname
FinAlgoritmo