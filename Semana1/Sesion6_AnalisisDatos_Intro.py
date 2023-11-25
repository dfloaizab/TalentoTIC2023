# PRACTICA WORKLOW ANÁLISIS DE DATOS
# QUÉ ES EL ANÁLISIS DE DATOS?
# PROCESO SISTEMÁTICO DE APLICAR TÉCNICAS DE CARGA, LIMPIEZA, ANÁLISIS ESTADÍSTICO DE DATOS
# EVALUAR Y APOYAR LA TOMA DE DECISIONES
#
#
# WORKFLOW DA:
# 1. CARGA DE DATOS -> 2. LIMPIEZA DE DATOS -> 3. ANÁLISIS -> 4. VISUALIZACIÓN 

import pandas as pd

#función propia para eliminar varias columnas nulas del dataframe:
def drop_columns(df:pd.DataFrame, columns_list):
    for col_name in columns_list:
        df.drop(col_name,inplace=True,axis=1)

#carga del dataset:
df_police = pd.read_csv("police.csv")
df_police.info()

#limpieza del dataset:
#limpieza de columnas con valores nulos:
cols = ["county_name","search_type"]
drop_columns(df_police,cols)
df_police.dropna(inplace=True)
df_police.info()

#renombrar columna "driver_age_raw":
df_police.rename(columns={"driver_age_raw":"birth_year"},inplace=True)
df_police.info()

#validar datos:
#conversion de formato:
# verificar python data types

#convertir estas dos columnas a entero
df_police = df_police.astype({"birth_year":"int64"})
df_police = df_police.astype({"driver_age":"int64"})

#print(df_police.head(10)) #10 primeras filas del dataframe
#print(df_police.tail(10)) #10 últimas filas del dataframe

#validar rango de valores de las columnas:
#iterar en el dataframe:

media_anio = df_police["birth_year"].mean()

# año de nacimiento (birth_year):
for i, row in df_police.iterrows():                          #invocamos la función iterrow para crear un iterador sobre las 
    if row["birth_year"] <= 1900 or row["birth_year"] >= 1987: #filas del dataframe: i, indice de la fila. item, info de la fila
                                                              #validar que el año corresponda a un mayor de edad
        #opción 1: asignar un valor que pueda corresponder al promedio
        df_police.loc[i,"birth_year"] = media_anio

        #opción 2: eliminar la columna:                                                            
        #df_police.drop(i)

# corregir edad (driver_age):

# obtener media de la columna:
media_edad = df_police["driver_age"].mean()

#Corregir:
for i, row in df_police.iterrows():                          #invocamos la función iterrow para crear un iterador sobre las 
    if row["driver_age"] < 12 or row["driver_age"] > 70: #filas del dataframe: i, indice de la fila. item, info de la fila
                                                              #validar que el año corresponda a un mayor de edad
        #opción 1: asignar un valor que pueda corresponder al promedio
        #print("Se va a corregir valor de la edad:")
        df_police.loc[i,"driver_age"] = media_edad

        #opción 2: eliminar la columna:                                                            
        #df_police.drop(i)

print(f"Edad máxima:{df_police['driver_age'].max()}")

# INTRODUCCIÓN A LA FASE 3 DEL WORKFLOW

# (a) SELECCIÓN DE UN SUBCONJUNTO DE COLUMNAS DEL DATAFRAME

df_police_sub = df_police[ ["stop_date","stop_time","driver_gender","driver_age","violation_raw","is_arrested","drugs_related_stop"]  ]

# df_police_sub.info()
# print(df_police_sub.head(10))
# df_police_sub.to_json("police_inf2005.json")
# df_police_sub.to_xml("police_inf2005.xml")

# (b) FILTRADO DEL DATAFRAME (SOLO FILAS QUE CUMPLAN CONDICIONES SOBRE UNA O VARIAS COLUMNAS)
df_police_sub_under_40 = df_police_sub[ df_police_sub["driver_age"] < 40  ]
#print(df_police_sub_under_40)


#------   TIPOS DE FUNCIONES DE ANÁLISIS EN DATASETS USANDO PANDAS  --------
# (a) obtener parámetros estadísticos de columnas

print(df_police_sub.describe())
print(df_police_sub.info())
print(f"Edad mínima:{df_police_sub['driver_age'].min()}")
print(f"Edad máxima:{df_police_sub['driver_age'].max()}")

# (b) Análisis de correlación 
#     por defecto, lo realizar para columnas numéricas
#df_police_sub.corr()

# (c) crear análisis de correlación para columnas no-numéricas:
#       (1) crear categorías/etiquetas para columnas no numéricas (driver_gender,violation_raw, is_arrested,drugs_related_stop)
#       (2) invocar la función corr sobre las nuevas columnas
#  crea una columna para cada categoría posible (M, F) y un valor de 0 o 1 en cada fila, según pertenezca
#  a la categoría o no
print(df_police_sub["driver_gender"].str.get_dummies())

#       (3) factorizar las columnas no numéricas con el fin de crear una
#           una representación numérica de estas
#df_police_sub.apply(     lambda x : x.factorize()[2]    )
#print(df_police_sub)
#       (4) usar libreria de ML para generar valores para las etiquetas

df_sub2 = df_police_sub[  ["driver_age","violation_raw","is_arrested","drugs_related_stop"]   ]
df_sub2 = df_sub2.apply( lambda x: pd.factorize(x)[0] )
print(df_sub2)
print("Correlación entre edad y tipo de infracción:")
# obtiene los coeficientes de correlación entre las distintas columnas de forma matricial:
# [-1.0,1.0]
# correlación perfecta es 1.0
# correlación alta > 0.6
# correlación negativa entre A,B implica que si aumenta el valor de A, dismunuye B 

print(df_sub2.corr())
