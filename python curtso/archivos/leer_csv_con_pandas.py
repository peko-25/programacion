import pandas as pd

#usando funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv") #, names=["name",'lastname','ege']) agregando esto podes agregar un encabezado

df2 = pd.read_csv("archivos\\datos.csv")
#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por edad
df_ordenado_as = df.sort_values("edad")

#ordenando de forma decendente
df_ordenado_de = df.sort_values("edad",ascending=False)

#concatenar df
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 2 filas con head()
primeras_filas = df.head(2)

#accediendo a las ultimas 2 filas con tail()
ultimas_filas = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadisticas del dataframe
df_info = df.describe()

#accediendo a un elemento especifico con loc
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elemento especifico con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellidos_loc =df.loc[:,"apellidos"]

#accediendo a todas las filas de una columna
apellidos_iloc =df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 =df.loc[2,:]

#accediendo a la fila 3 con iloc
fila3 =df.iloc[2,:]

#accediendo a dilas con edad mayor que 30
moyor_que_30 = df.loc[df["edad"]<30,:]



print(moyor_que_30)