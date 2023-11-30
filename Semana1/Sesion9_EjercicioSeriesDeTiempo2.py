import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime

df_crimes_balt = pd.read_csv("Datasets/TimeSeries/BaltimoreCrimeData2.csv")

df_crimes_balt.drop(columns="Weapon", inplace=True, axis=1)
print(df_crimes_balt.info())

df_crimes_sub = df_crimes_balt[ ["CrimeDate","CrimeTime","Total Incidents","Neighborhood","Description","Location","District"]  ]

df_crimes_sub = df_crimes_sub.dropna()
df_crimes_sub.info()

#concatenar para la nueva columna de tiempo:
df_crimes_sub["datetime"] = df_crimes_sub[["CrimeDate","CrimeTime"]].apply(lambda x: " ".join(x), axis=1 )
print(df_crimes_sub.info())

#formatear columna de fecha (con coerce = true para asignar NaN a los valores que no pueda convertir):
df_crimes_sub["datetime"] = pd.to_datetime( df_crimes_sub["datetime"],errors="coerce")

df_crimes_sub = df_crimes_sub.dropna()


#con opción format (averiguar cuál?):
#df_crimes_sub["datetime"] = pd.to_datetime( df_crimes_sub["datetime"],format='%m/%d/%Y-%H:%M:%S',errors="coerce")

df_crimes_sub["current_datetime"] = datetime.now()
print(df_crimes_sub.head())
print(df_crimes_sub.info())

#eliminar dupplicados
#df_crimes_sub.drop_duplicates(inplace=True)
# print(df_dup.info())

#filtrar por distrito:
#df_filt1 = df_crimes_sub[ df_crimes_sub["Neighborhood"] == "Westfield"   ]
#df_filt1.info()
df_crimes_sub.fillna(value=0)
#Convertir a una tabla pivote (donde se construya el índice de la tabla a partir de la info temporal):
# pivot_table permite valores duplicados a partir del índice:
# pivot no permite valores duplicados
df_crimes_pivot = df_crimes_sub.pivot_table(index=["datetime"], columns=["District"],values="Total Incidents",aggfunc="sum",fill_value=0)



print(df_crimes_pivot.head(100))

#continura el ejercicio...

#agrupamientos y agregaciones para visualización


#visualización de datos muestreados en una frecuencia distinta
fig, axes=plt.subplots(1,2)
df_crimes_pivot.resample("M").sum().plot(kind="bar",ax=axes[0], rot=0)
df_crimes_pivot.resample("W").sum().plot(kind="bar",ax=axes[1], rot=0)
plt.show()
