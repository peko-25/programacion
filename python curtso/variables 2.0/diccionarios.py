#crando dicionarios con dict()
diccionario = dict(nombre="felipe",apellidp="mendieta")

#las litas no pueden ser claves y usamos frouxenset para meter conjuntos
diccionario = {frozenset(['dalto','rancio']):'jsdjsjd'}

#creando diccionarios con fronkeys() valor por defecto none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fronkeys() cambiando el valor por defecto "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"no se")




print(diccionario)