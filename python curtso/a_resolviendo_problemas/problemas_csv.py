#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("a_resolviendo_problemas\\datos.csv")

#cambiando lo datos de eda a str
df['edad'] = df['edad'].astype(str)

#mostrando el typo de dato
#print(type(df['edad'][0]))

#remplazar un dato por otro
df['apellidos'].replace('dalto','maestro', inplace=True)

#eliminando las filas con datos faltantes
df =df.dropna()#df.dropna(exis=1) para elimina las colomnas con datos faltantes

#eliminando las filas repetidas
df = df.drop_duplicates()

#creando un cvs con el dataframe resultante (limpio)
df.to_csv("a_resolviendo_problemas\\datos_limpio.csv")

print(df)