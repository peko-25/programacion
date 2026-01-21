with open("archivos\\texto_feli.txt",'a',encoding="UTF-8") as archivo:
    #usando un bucle pára agregar varias lineas
    for i in range(25):
        archivo.write(f"\nlinea {i+1} agregada")
