import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


#---------------------- DATASET 1: MORTALIDAD TUBERCULOSIS ------------------------

#1. carga y selección de columnas
df_tub_caldas = pd.read_csv("Mortalidad_tuberculosis_2010_a_2016_20231125.csv",encoding="utf-8")
df_sub = df_tub_caldas[  ["SEXO","EST_CIVIL","EDAD","NIVEL_EDU","OCUPACION","CODMUNRE","SEG_SOCIAL","MUERTEPORO"]   ]

df_sub.dropna(inplace=True)
df_sub.info()

#imprimir valores únicos de una columna:
print(f"Valores est civil:{df_sub['EST_CIVIL'].unique().__len__()}")
print(df_sub["EST_CIVIL"].unique())

#2. limpieza / corrección 
#se identifican algunos valores que difieren en un espacio:

#iterar sobre todas las filas y eliminar espacios al inicio y final de esta
#columna para normalizar los datos
for i, row in df_sub.iterrows():
    df_sub.loc[i,"EST_CIVIL"] = str(row["EST_CIVIL"]).strip()
    df_sub.loc[i,"NIVEL_EDU"] = str(row["NIVEL_EDU"]).strip()

print(f"Valores est civil:{df_sub['EST_CIVIL'].unique().__len__()}")
print(df_sub["EST_CIVIL"].unique())


print(df_sub["NIVEL_EDU"].unique())
print(df_sub["SEXO"].unique())

#filtrado de filas
df_sub_f = df_sub[  df_sub["SEXO"] == "Femenino"  ]
df_sub_m = df_sub[  df_sub["SEXO"] == "Masculino"  ]

print(df_sub["MUERTEPORO"].unique())

#3. factorización (para análisis de correlación)
df_sub = df_sub.apply(lambda x: pd.factorize(x)[0])
corr1 = df_sub.corr()

plt.figure(figsize=(10,10))
sb.heatmap(corr1, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5) #
plt.title("Matriz de Correlación - Mortalidad Tuberculosis Caldas - 2010/2016" )
plt.show()

#----------------- DATA SET 2: PERFIL DE MORBILIDAD --------------

df_perf_morb = pd.read_csv("Perfil_de_morbilidad_20231125.csv")
df_perf_morb.info()

print(df_perf_morb["DESTINO AL EGRESO"].unique().__len__())
print(df_perf_morb["NOMBRE DEL DIAGNOSTICO"].unique().__len__())

df_dup = df_perf_morb[  df_perf_morb.duplicated()  ]
print(df_dup)
df_perf_morb.drop_duplicates(inplace=True)
df_perf_morb.info()

#renombrar columnas:
df_perf_morb.rename(columns={"CIDIGO CIE-10":"Cod","NOMBRE DEL DIAGNOSTICO":"Nombre","EDAD DE ATENCION (AÑOS)":"Edad","AÑO REPORTADO":"Año"},inplace=True)

#factorizar y hacer análisis de correlación:
df_perf_morb = df_perf_morb.apply(lambda x: pd.factorize(x)[0])
corr = df_perf_morb.corr()

#mostrar correlación con un mapa de calor:
plt.figure(figsize=(10,10))
sb.heatmap(corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5)
plt.title("Matriz de Correlación")
plt.show()






