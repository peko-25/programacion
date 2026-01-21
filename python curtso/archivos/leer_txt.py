#usando opne para abrir un archivo con una codificacion universal(UTF-8) a archivos
archivo = open("archivos\\texto_feli.txt")
#leer todo
archivo = archivo.read()

#leer por linea
#linea = archivo.readlines()

#leer una sola linea
#linea = archivo.readline()

#cerrar el archivo
archivo.close()

print(archivo)
