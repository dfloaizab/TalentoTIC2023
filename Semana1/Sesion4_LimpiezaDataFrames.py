#Talento TICs 2023 - Python 2 (python para analítica de datos)
# Sesión 4 - Limpieza de dataframes (Noviembre 22)
# PRONTO EMPEZAMOS, GRACIAS POR LA ESPERA

import pandas as pd
import numpy as np

 #Problemas típicos en un dataframe (asumiendo que el archivo se cargue de forma correcta):
    # 1. datos nulos o faltantes (a veces, columnas completas)
    # 2. filas/datos duplicados
    # 3. datos incorrectos
    #   3.1 formato de datos
    #   3.2 valor/rango de datos


    # 4. índices incorrectos
    # 5. formatos de nombres de columnas o nombres incorrectos
    # 6. consumo de memoria (dataframe demasiado grande)

    # (a) se carga el dataframe desde el archivo plano
df_air_quality = pd.read_csv("Air_Quality_Dirty.csv")

# (b) visualizar información del dataframe:
df_air_quality.info()

#----- 1. datos nulos o faltanes en un dataframe:

#se identificó una columna donde todos los valores son nulos, descartar columna
# se usa la función drop : nombre de la columna, elimina en el mismo dataframe, 
# axis corresponde al eje del dataframe: axis = 1, corresponde a las columnas (eje vertical)
#                                       axis = 0, corresponde a las filas (eje horizontal)
df_air_quality.drop("Message",inplace=True,axis=1)
df_air_quality.info()

# se eliminan después todas las filas en las que al menos una columna tenga un valor vacío
df_air_q_clean1 = df_air_quality.dropna()
df_air_q_clean1.info()

#---------- 2. Verificar Duplicados 
#mostrar qué filas están duplicadas:
print(df_air_q_clean1.duplicated())

df_dup = df_air_q_clean1[df_air_q_clean1.duplicated()]
print(df_dup.info())
print(df_dup)


#eliminar filas duplicadas del dataframe:
df_air_q_clean1.drop_duplicates(inplace=True)

#----------- 3. Corregir formato de datos
df_meteo = pd.read_csv("Meteorite_Landings_Dirty.csv")
df_meteo.info()

#eliminar valores nulos:
df_meteo.dropna(inplace=True)
df_meteo.info()

#eliminar duplicados:
print(df_meteo.duplicated())

df_meteo_dup = df_meteo[df_meteo.duplicated()]
print(df_meteo_dup)

df_meteo.drop_duplicates(inplace=True)
df_meteo.info()

# (!!!!!) ¿CÓMO IDENTIFICAR ESTE TIPO DE ERRORES?
# ESTRATEGIA: Identificar de antemano cuáles son las columnas importantes en las tareas de análisis de datos
# y proceder a "corregirlas" o "analizarlas"
# validando el rango o encontrando datos atípicos
# 3.1 eliminar errores de formato de datos (cuando se identifica columna específica):
df_meteo = df_meteo.astype({"year":"int64"})

print(df_meteo.head(10).to_string())


# 3.2 corregir errores de valores / rango de datos (identificar las filas en las que suceden)
#     se debe iterar en el dataframe para la columna que quiero corregir o validad:
for i,item in df_meteo.head(15).iterrows():
    if item["year"] < 1900 or item["year"] > 2023:
        print(item)
        #corregir el año:
        df_meteo.loc[i,"year"] = 1900


print(df_meteo.head(15))
