Proceso ValidarDNI
    Definir dni Como Cadena
    Definir long_dni Como Entero
    Definir es_valido Como Entero
    Definir i Como Entero
    Definir dni_formateado Como Cadena
    Definir sub_dni Como Caracter
	
    Repetir
        Escribir "Ingrese su DNI sin puntos, guiones ni espacios: "
        Leer dni
        long_dni <- Longitud(dni)
        es_valido <- 0
		
        // Validar que no tenga puntos, guiones ni espacios
        Para i <- 1 Hasta long_dni Hacer
            sub_dni <- Subcadena(dni, i, i)
            Segun sub_dni Hacer
                ".":
                    es_valido <- es_valido + 1
                " ":
                    es_valido <- es_valido + 1
                "-":
                    es_valido <- es_valido + 1
            Fin Segun
        FinPara
		
        // Validar que la longitud esté entre 1 y 8 caracteres
        Si long_dni < 1 O long_dni > 8 O es_valido >= 1 Entonces
            Escribir "Error: El DNI debe tener entre 1 y 8 caracteres, y no contener puntos, guiones ni espacios."
        FinSi
    Hasta Que long_dni >= 1 Y long_dni <= 8 Y es_valido = 0
	
    // Rellenar con ceros a la izquierda si tiene menos de 8 caracteres
	yoqc<-SubCadena("00000000", 1, 8 - long_dni)
	Escribir yoqc
    dni <- Concatenar(yoqc, dni)
	Escribir dni
    // Formatear el DNI con puntos como separadores de miles y millones
	sub_dni1<-SubCadena(dni,1,2)
	sub_dni2<-SubCadena(dni,3,5)
	sub_dni3<-SubCadena(dni,6,8)
	Escribir sub_dni1 "--" sub_dni2 "--" sub_dni3 
    dni_formateado <- Concatenar(sub_dni1,".")
	Escribir dni_formateado
	dni_formateado<- Concatenar(dni_formateado,sub_dni2)
	Escribir dni_formateado
	dni_formateado<- Concatenar(dni_formateado,".")
	Escribir dni_formateado
	dni_formateado<-Concatenar(dni_formateado,sub_dni3)
	Escribir dni_formateado
    // Mostrar el DNI formateado
    Escribir "Su DNI es: ", dni_formateado
FinProceso
