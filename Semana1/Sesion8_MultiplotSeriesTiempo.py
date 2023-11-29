

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Cargar el dataframe:
df_CD_medic = pd.read_csv('Datasets/CODIGO_MEDICAMENTOS_VIGENTES.csv')

#df_Sab11.info()

# Limpieza del dataframe:
df_CD_medic.dropna(inplace=True)
#df_Sab11.info()

# Se identifican las filas están duplicadas:
#print(df_Sab11.duplicated())
df_CD_medic.drop_duplicates(inplace=True)

# Se seleccionan las columnas para analizar
df_CD_Medic1 = df_CD_medic[["expediente", "producto", "registrosanitario", "fechavencimiento", "formafarmaceutica", "viaadministracion"]]
df_CD_Medic1.info()

# Se realiza la factorizacion:
df_CDM = df_CD_Medic1.apply(lambda x: pd.factorize(x)[0])
print(df_CDM.corr())

#CREAR MÚLTIPLES PLOTS

fig, axes = plt.subplots(3,2)

#axs retorna las coordenadas donde debe ir cada subplot:
#axes = [0,0], [0,1]
#       [1,0], [1,1]
#       [2,0], [2,1]

# Se grafican los datos por tabla de calor  
plt.figure(figsize=(10,10))
corr = df_CDM.corr()
sb.heatmap(corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5,ax=axes[0,0]) #
plt.title("Correlacion Medicamentos Vigentes" )
#plt.show()

#grafico de agrupacion:

sb.histplot(df_CDM["producto"], bins=20, kde=True,ax=axes[0,1])
plt.title("Los medicamentos que se encuentran vigentes")
#plt.show()

sb.violinplot(x="formafarmaceutica", y="viaadministracion", data=df_CDM, inner="quartile",ax=axes[1,0])
plt.title("Comparacion ")
#plt.show()

sb.boxenplot(x="producto", y="registrosanitario", data=df_CDM,ax=axes[1,1])
plt.title("Registro sanitario de cada producto")
#plt.show()


sb.boxplot(x="producto", y="fechavencimiento", data=df_CDM,ax=axes[2,0])
plt.title("Fecha de vencimiento por cada producto")

#plt.show()

# --------   ANÁLISIS DE SERIES DE TIEMPOS --------
df_air_quality = pd.read_csv("Datasets/AirQualityParis.csv",parse_dates=["date.utc"])
df_air_quality = df_air_quality.rename(columns={"date.utc":"datetime"})
print(df_air_quality.head())
print(df_air_quality.info())

print(df_air_quality["city"].unique())

#adecuar la columna de la serie de tiempo al formato correcto
#esta función de conversión funciona cuando el formato de fecha viene 
#correcto desde el dataframe
df_air_quality["datetime"] = pd.to_datetime(df_air_quality["datetime"])
print(df_air_quality.info())

#obtener fecha mínima y máxima:
print(f"fecha mínima:{df_air_quality['datetime'].min()}")
print(f"fecha máxima:{df_air_quality['datetime'].max()}")

df_air_quality["month"] = df_air_quality["datetime"].dt.month

print(df_air_quality["month"])

#---- Funciones de Agrupación y agregación:
#Ej: Concentración promedio de NO2 agrupado por  día de la semana y ubicación de la medición:
fig, axes=plt.subplots(1,1)
print(df_air_quality.groupby( [df_air_quality["datetime"].dt.weekday,"location" ] )["value"].mean())

#--- graficar comportamiento de la medición por hora del día
df_air_quality.groupby( df_air_quality["datetime"].dt.hour  )["value"].mean().plot(kind="bar",rot=0,ax=axes)

plt.xlabel("Hora del día")
plt.ylabel("$NO_2 (µg/m^3)$")
#plt.show()

#--- Usar columna fecha como un índice del dataset (pivote):
pvt_air_quality = df_air_quality.pivot(index="datetime", columns="location",values="value")
print(pvt_air_quality.head())

#--- graficar desde la tabla pivote en un determinado rango de fecha:
pvt_air_quality["2019-05-20":"2019-05-21"].plot()
#plt.show()

#--- remuestreo de la serie de tiempo a una nueva frecuencia (frecuencia mensual)
print("Maximo mensual:\n")
maximo_mensual = pvt_air_quality.resample("M").max()
print(maximo_mensual)

#--- remuestreo de la serie de tiempo a una nueva frecuencia (frecuencia diaria) para mostrar la media en las
# distintas localizaciones
pvt_air_quality.resample("D").mean().plot(style="-o",figsize=(10,5))
#plt.show()

#--------- ANÁLISIS DE VARIOS DATASETS ----------------

df1 = pd.read_csv("Datasets/Parte1.csv")
df2 = pd.read_csv("Datasets/Parte2.csv")

# merging y concatenación de varios datasets:

#concatenación de dos dataframes de forma vertical
df_r1 = pd.concat([df1,df2], axis=0)
print(df_r1.info())

# fusión de dos dataframes por una columna común:
# PENDIENTE
df_c1 = pd.merge(df1,df2,on="Unique ID",how="inner")
print(df_c1.info())




