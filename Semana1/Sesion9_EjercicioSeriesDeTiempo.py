#Talento TICs 2023
# EJERCICIOS SERIES DE TIEMPOS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#carga del dataset:
df_temps = pd.read_csv("Datasets/TimeSeries/MinTemperatures.csv",parse_dates=["Date"])

#adecuación del dataset para manejo de datos temporales:
print(f"dataset sin limpiar:{df_temps.info()}")

df_temps = df_temps.rename(columns={"Date":"datetime","Daily minimum temperatures":"temps"})

#valores inválidos con opción errors = "coerce", asigna NaN:
df_temps["temps"] = pd.to_numeric(df_temps["temps"],errors="coerce") 
df_temps.dropna(inplace=True)

print(f"dataset limpio:{df_temps.info()}")
print(df_temps.head(100))

print(df_temps["datetime"].min())
print(df_temps["datetime"].max())

#para plotear los datos de la serie temporal debemos crear una tabla pivote en la cual
#el índice sea la fecha
pvt_temps = df_temps.pivot(index="datetime",values="temps",columns="temps")
#plotear en un rango de fecha:
#pvt_temps["1/1/1990":"1/30/1990"].plot(style="-o", figsize=(10,5))
plt.xlabel("dias")
plt.ylabel("temperaturas")
plt.title("Temperaturas por mes 1989 - 1990")


#resamplear y mostrar por mes:}
fig, axes = plt.subplots(1,1)
print(pvt_temps.head())
pvt_temps["1/1/1989":"1/30/1990"].resample("M").mean().plot(style="o", figsize=(10,5))
#sb.barplot(data=pvt_temps["1/1/1989":"1/30/1990"].resample("M").mean(),y="temps")
plt.show()