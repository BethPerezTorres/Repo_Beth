# 1) Crear una función llamada "df_ordered" que reciba un dataframe y un str y retorne un
# dataframe ordenado de mayor a menor considerando la característica str.
import pandas as pd
import numpy as np

#AQUI HACEMOS NUESTRA TABLA CON DATOS
array = np.random.uniform(0, 10, size=[8,4])
df = pd.DataFrame(array, index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], columns=['W', 'X', 'Y', 'Z'])
print(type (df))
print(df)

#AQUI CREAMOS NUESTRA FUNCION
def def_ordered(df: pd.DataFrame, column):
    if column not in df.columns:
        raise ValueError(f"La columna '{column}' no existe en el DataFrame.")

    df_sorted = df.sort_values(by=column, ascending=False)
    return df_sorted

#AQUI DAMOS ULTIMAS INDICACIONES: ORDENAR LAS FILAS DE MAYOR A MENOR SEGUN LA COLUMNA W
df_ordenado = def_ordered(df, 'W')
print(df_ordenado)

#SI PONEMOS UNA COLUMNA QUE NO EXISTE NOS ARROJA UN ERROR
#df_ordenado = def_ordered(df, 'A')
#print(df_ordenado)

#_____________________________________________________________________________________________________________________

# 2) Crear una función llamada "plot_bar" que reciba un dataframe y un str y haga el plot
# de barras de ese dataframe considerando esa caracterísitca descrita por el string
import pandas as pd

#AQUI DEFINIMOS LOS DATOS DE NUESTRA TABLA
data = {'Categoría': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C'],
        'Valores': [10, 15, 10, 25, 15, 10, 25, 25]}
df1 = pd.DataFrame(data)
print(type (df1))
print(df1)

import seaborn as sns
import matplotlib.pyplot as plt

#AQUI DEFINIMOS NUESTRA FUNCIÓN
def plot_bar(df1, column):
    if column not in df1.columns:
        raise ValueError(f"La columna '{column}' no existe en el DataFrame.")

    #AQUI ESPECIFICAMOS CARACTERISICAS DE NUESTRA TABLA
    count_data = df1[column].value_counts().reset_index()
    count_data.columns = [column, 'counts']
    plt.figure(figsize=(10, 6))
    sns.barplot(x=column, y='counts', data=count_data)
    plt.title(f'Gráfico de barras de {column}', fontsize=16)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.show()

#PLOT A PARTIR DE NUESTRO STR 'CATEGORIA'
plot_bar(df1, 'Categoría')

#_____________________________________________________________________________________________________________________

# 3) países con mayor depresión
file_path = '/home/bubbleth/PycharmProjects/pythonProject/Repo_Beth/MENTALPREV.csv'
df2 = pd.read_csv(file_path)

#SUMAR EL VALOR DE DEPRESIÓN A LO LARGO DE LOS AÑOS PARA CADA PAÍS
df2_depression = df2.groupby('Entity')['Depressive disorders (share of population) - Sex: Both - Age: Age-standardized'].sum()

#SELECCIONAR LOS SEIS PAISES CON UN VALOR MAS ALTO
top_6_countries = df2_depression.nlargest(6)
print(top_6_countries)

#_____________________________________________________________________________________________________________________

# 4) gráfica de barras mostrando el valor de depresión y la entidad (país)
import matplotlib.pyplot as plt

#AQUI CREAMOS LA GRAFICA DE BARRAS PARA LOS PAISES CON VALORES MAS ALTOS Y ESPECIFICAMOS
#ALGUNAS CARACTERISTICCAS DE NUESTRA IMAGEN
top_6_countries.plot(kind='bar', color='skyblue')
plt.xlabel('País')
plt.ylabel('Total de Depresión (Acumulado)')
plt.title('Top 6 Países con Mayor Depresión')
plt.tight_layout()
plt.show()

#_____________________________________________________________________________________________________________________

# 5) países con mayor desorden alimenticio
# 6) gráfica de barras mostrando el valor de desorden alimenticio y la entidad (país)

# 7) países con mayor esquizofrenia
# 8) gráfica de barras mostrando el valor de esquizofrenia y la entidad (país)

# 9) crear un data frame con los valores por país de ["Entity Code", "Year", "Schizophrenia disorders", "Depressive disorders", "Anxiety disorders", "Bipolar disorders", "Eating disorders"]
# 10) mostrar los estadísticos del dataframe anterior

# 11) mostrar la distribución de cada feature del dataframe anterior
# 12) mostrar en un mapa de color la correlación entre las features ["Schizophrenia disorders", "Depressive disorders", "Anxiety disorders", "Bipolar disorders", "Eating disorders"]

# 13) Del dataset cancer_reg visto en clase, determinar:

# la correlación entre las features [ 'target_deathrate', 'avganncount', 'avgdeathsperyear', 'incidencerate', 'medincome', 'povertypercent', 'pctprivatecoverage', 'pctpubliccoverage' ]
# mostrar la distribución de cada feature del dataframe anterior
# aquellos que dependencia lineal encontrar los valores de la recta. hint: scipy