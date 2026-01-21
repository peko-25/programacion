#lista se puede modificar

lista = ["feli mendieta","soy feli",True,1.85]

#tupla no se puede modificar

tupla = ("feli mendieta","soy feli",True,1.85)

#valido
lista[0] = "feli"

#no valido

#tupla[0] = "feli"

#creando conjuento set (no se accede al indicew)

conjunto = {"feli mendieta","soy feli",True,1.85}

#conjunto[1] = "jeje"
conjunto = {"jaja maquiena t jodi"}
#print(conjunto[3]) (no deja ver)

#creando un didct
dicionario = {
    'nombre' : "feli",
    'apellido' : "mendieta",
    'ea' : True,
    'flotante' : 1.85
}
print(dicionario['ea'])