cadena1 = "hola soy feli"
cadena2 = "bienvenido bro"
cadena3 = "239742"
cadena4 = "holacomoestas"
#print(dir(cadena1))
 
Buesq_find = cadena1.find("q")# si nno encuentra devueklve -1

#Buesq_index = cadena1.index"l"#si no encuentra nd tira error (excepcion)

es_numerico = cadena3.isnumeric()#si es numerico devuelve true de lo contario false

es_alf_numerico = cadena4.isalpha()#si hay caractecteres especiales devuelve false

resultado = cadena1.count("a")#cuenta concidencias 

contar_caracteres = len(cadena1)#cuenta los caracteres

empieza_con = cadena1.startswith("ho")#verifica que empieze con lo que pones

termina_con = cadena1.endswith('li')#verifica que termine con lo que pones

cadena_nueva= cadena1.replace(",", " ")# remplasa la concidencia con lo nuevo

cadena_separada = cadena1.split(" ")





 
print(cadena_separada)