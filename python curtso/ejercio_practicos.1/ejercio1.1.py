#promedios de duracion cursos 
otro_min = 2.5
otro_max = 7
dalto_curso = 1.5
otros_promedio = 4

#el crudo del materia
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de los cursos
diferencia_min = 100 - (dalto_curso / otro_min * 100)
diferencia_max = round(100 - (dalto_curso / otro_max * 100),1)
diferencia_promedio = 100 - (dalto_curso / otros_promedio * 100)

#mostrar el % menos
print("--------------------------")
print(f"el curso de dalto dura un {diferencia_min}% menos que el mas rapido")
print(f"el curso de dalto dura un {diferencia_max}% menos que el mas lento")
print(f"el curso de dalto dura un {diferencia_promedio}% menos que el promedio")
print("--------------------------")

# % de material inservible que se reduce
prosentaje_reducido_pro = round(100 - (otros_promedio / crudo_promedio * 100),1)
prosentaje_reducido_dalto = round(100 - ( dalto_curso  / crudo_dalto * 100),1)

#REDONDEANDO NUMEROS



#mostrar el promedio
print(f"un curso promedio elimina un {prosentaje_reducido_pro}% de tiempo vacio")
print(f"este elimina un {prosentaje_reducido_dalto}% del tiempo vacio")
print("--------------------------")

#mostrando diferencias si duraran 10h los cursos
print(f"ver 10 horas de este curso equivale a {otros_promedio *100 // dalto_curso /10} horas de otro")
print(f"ver 10 horas de otro curso equivale a {dalto_curso *100 // otros_promedio /10} horas de este curso")
print("--------------------------")





