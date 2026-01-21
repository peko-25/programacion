#dos listas unas con nombres y apellidos
nombre = ['lucas','jhon','dalto']
apellido = ['dalño', 'whik','luñas']

#registrar esta informacion en un txt de manera optima
with open("resolviendo_problemas\\nombres_apellidos.txt",'w',encoding="UTF-8")as archivo:
    
    archivo.writelines('los datos son: \n\n')
    [archivo.writelines(f"nombre: {n} \napellido: {a}\n------------------\n") for n,a in zip(nombre,apellido)]