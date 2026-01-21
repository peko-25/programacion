
#abriendo el archivo with opnes
with open("archivos\\texto_feli.txt",encoding="UTF-8") as archivo :
    
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
#nio es necesario cerrarlo al usar with open