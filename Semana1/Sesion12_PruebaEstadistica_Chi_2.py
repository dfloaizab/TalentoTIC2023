#Talento TICs 2023
# Python para análisis de datos

# Prueba de chi-cuadrado : prueba que determina la dependencia entre dos
# variables categóricas en una muestra de datos. se realiza sobre una tabla de contingencia, 
# analizando las frecuencias de las variables

#hipótesis nula: "no hay dependencia entre las variables a analizar"


import pandas as pd
from scipy.stats import chi2_contingency, chi2

# Tabla de contingencia:
# tabla que resume las  frecuencias de unas variables categóricas

#Ejemplo: géneros escuchados por ciudad:

data = {
    "Documento": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    "Ciudad_Persona": ["Cali", "Cali", "Medellin","Bogotá","Bogotá","Barranquilla","Barranquilla","B/Manga","Cartagena","Cúcuta","Pereira","Manizales","Pasto","Cali","Bogota","Medellin","Cali","Cali","Cali"],
    "Genero_Escucha" : ["Salsa","Rock","Reggaeton","Salsa","Rock","Salsa","Rock","Reggaeton","Champeta","Salsa","Tropipop","Tango","Vallenatos","Salsa","Rock","Reggaeton","Salsa","Salsa","Salsa"]
}

df_generos = pd.DataFrame(data)
print(df_generos)

#se genera la tabla de contingencia (frecuencia de las variables categóricas):
tb_cont = pd.crosstab(df_generos["Ciudad_Persona"],df_generos["Genero_Escucha"])
tb_cont_totales = pd.crosstab(df_generos["Ciudad_Persona"],df_generos["Genero_Escucha"],margins=True,margins_name="Total")

print(tb_cont)
print(tb_cont_totales)

# Prueba de chi-cuadrado sobre la tabla de contingencia (frecuencia de datos categóricos)
chi2, p,a,b = chi2_contingency(tb_cont)
print(f"Parámetro Chi 2:{chi2}")
print(f"Parámetro p:{p}")

alpha = 0.05 #nivel de significancia de la prueba

#
if p < alpha:
    # se rechaza la hipótesis nula, es decir, SÍ ha dependencia entre los datos
    print("se rechaza la hipótesis nula, es decir, SÍ ha dependencia entre los datos")
else:
    # se acepta la hipótesis nula, es decir, NO hay dependencia entre los datos
    print("se acepta la hipótesis nula, es decir, NO hay dependencia entre los datos")


#Ejercicio sobre dataset saber11.csv:

#crear una muestra con las siguientes columnas:
#ESTU_MCPIO_RESIDE, FAMI_TIENECOMPUTADOR, FAMI_NUMLIBROS, FAMI_SITUACIONECONOMICA

# data = {
#     "id" : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
#     "nacionalidad" : [ "Colombiano", "Norteamericano", "Italiano",....],
#     "mano_habil": ["Diestro","Zurdo",....]
# }

#EJERCICIO: Dataset saber11.csv 
# convertir datos de puntajes a escala categorica
# aplicar prueba estadística chi cuadrado 

#cargar el dataset
df_icfes = pd.read_csv("Datasets/saber11.csv")

#encontrar el mínimo y el máximo para la variable que queremos convertir en una categoría:
print(df_icfes["PUNT_GLOBAL"].min())
print(df_icfes["PUNT_GLOBAL"].max())

#crear valores categóricos de acuerdo a la variable numérica en una nueva columna:
df_icfes['Nivel_Calif'] = pd.cut(x=df_icfes['PUNT_GLOBAL'], bins=[0, 177, 277, 377, 477], 
                     labels=['Low', 'Middle', 
                             'High',"Higher"]) 

#obtenemos la tabla de contingencia (tabla de frecuencias):
tb_cont = pd.crosstab(df_icfes["FAMI_ESTRATOVIVIENDA"],df_icfes["Nivel_Calif"])
print(tb_cont)

#se aplica prueba estadística a la tabla de contingengia, y se obtienen los valores
#estadísticos:
chi2, p,a,b = chi2_contingency(tb_cont)
print(f"Parámetro Chi 2:{chi2}")
print(f"Parámetro p:{p}")

#print(df_icfes.head())
#
if p < alpha:
    # se rechaza la hipótesis nula, es decir, SÍ ha dependencia entre los datos
    print("se rechaza la hipótesis nula, es decir, SÍ ha dependencia entre los datos")
else:
    # se acepta la hipótesis nula, es decir, NO hay dependencia entre los datos
    print("se acepta la hipótesis nula, es decir, NO hay dependencia entre los datos")
