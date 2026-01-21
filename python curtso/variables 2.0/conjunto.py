#creando un conjunto con set()
conjunto = set(["dato1",'dato2'])

#manteniando un conjunto dentro de otro
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
#verificar si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
#verificar si es superconjunto
resultado2 = conjunto1.issuperset(conjunto2)
resultado2 = conjunto1 > conjunto2

print(resultado)
print(resultado2)

#verificar si hay añgun numero en comun
resultado3 = conjunto2.isdisjoint(conjunto1)
print(resultado3)