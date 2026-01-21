dicionario = {
    'nombre' : "feli",
    'apellido' : "mendieta",
    'flotante' : 1.85
}

#nos devuelve un objeto dict_item
claves = dicionario.keys()

print(claves)

#encontrando un elemento con get() (si no encuentra nada el pograma continua)
valor_de_kasj = dicionario.get("kasj")
print(valor_de_kasj)

#eliminando un elemento del dicionario

# dicionario.pop("nombre")

print(dicionario)

#obteniendo un elemento dict_item iterable

dicionario_interable = dicionario.items()

print(dicionario_interable)