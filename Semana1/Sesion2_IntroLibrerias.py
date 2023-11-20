#Talento TICS 2023 - Python 2
#Noviembre 18, 203
# Pandas, Matplotlib, NumPy

#------------------- PANDAS -----------------------------

import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import random as r

print(pd.__version__)

#cargar o crear información (datasets o dataframes)

#1. Crear dataframe de forma manual:
data =  {
    "id": [1,2,3,4],
    "nombre": ["Zapatillas Converse","Zapatillas Nike","Zapatillas Adidas","Zapatillas Diesel"],
    "precio_unit": [250000.0,350000.0,380000.0,500000.0],
    "inv": [25, 25,30,15]
}

#Convertir diccionario de datos en python a dataframe de pandas:
df_calzado = pd.DataFrame(data)
print(df_calzado)

#procesando un dataframe en pandas:
print(df_calzado.info())

#seleccionando información de un dataframe:
print(df_calzado.head(2))
print(df_calzado.tail(2))

#selección de columnas: 
print(df_calzado["nombre"])

#selección de una fila en particular:
print(df_calzado.loc[2])

#obtener estadistica descriptiva de columnas numéricas de todo :
print(df_calzado.describe())

#obtener parámetro estadístico de una columna en particular:
print( f"Promedio de inventario: { df_calzado['inv'].mean()} ")
print( f"Mediana de inventario: { df_calzado['inv'].median()} ")
print( f"Moda de inventario: { df_calzado['inv'].mode()} ")

#agregar columna a un dataframe:
df_calzado["descuento"] = [0.1,0.15,0.2,0.25]
print(df_calzado)

df_calzado["bodega"] = ["centro", "centro", "sur", "norte"]
print(df_calzado)

#modificar datos  fila 1, columna inventario:
df_calzado.at[1,"inv"] = 30
print(df_calzado)

#eliminar columna:
df_calzado = df_calzado.drop("bodega", axis=1)
print(df_calzado)

#agregar fila:
nueva_fila = {"id": 1, "nombre": "Zapatillas Converse", "precio_u":250000.0, "inv":50}

#PENDIENTE

#eliminar fila:
df_calzado = df_calzado.drop(3)
print(df_calzado)


#operaciones entre columnas:
#ITERAR SOBRE UN DATA FRAME:
#1. agregar columna precio venta
df_calzado["precio_venta"] = [0.0,0.0,0.0]
print(df_calzado)

#ACTUALIZAR VALOR DE UNA COLUMNA DE UN DF CON BASE EN VALORES DE OTRAS COLUMNAS
#definir función de actualización:
def update_precio_venta(fila):
    return (fila["precio_unit"] - fila["precio_unit"] * fila["descuento"])

#recorrer filas
for fila in df_calzado.iterrows():
    print(fila)

#aplicar función de actualización
#df_calzado["precio_venta"] = df_calzado.apply(update_precio_venta, axis=1)
df_calzado["precio_venta"] = df_calzado.apply(  lambda fila: fila["precio_unit"] - fila["precio_unit"] * fila["descuento"], axis=1       )
print(df_calzado)

#----------------------------- MATPLOTLIB ---------------------------------
articulos = ["Zapatillas Converse","Zapatillas Nike","Zapatillas Adidas","Zapatillas Diesel"]
ventas_tienda_centro = [1500000,1800000,2000000,3000000]
ventas_tienda_sur = [2500000,1800000,4000000,3000000]
ventas_tienda_norte = [1800000,2200000,2000000,5000000]

#crear un gráfico de líneas:
plot.plot(articulos,ventas_tienda_centro,label="Ventas centro",marker='x' )
plot.plot(articulos,ventas_tienda_sur,label="Ventas sur",marker='x' )
plot.plot(articulos,ventas_tienda_norte,label="Ventas norte",marker='x' )

plot.xlabel("Articulos")
plot.ylabel("Ventas por tienda")
plot.title("Ventas por articulo en tienda")

plot.legend()

plot.show()


#------------------------------- NUMPY --------------------------------------
#NOVIEMBRE 18, 5 - 7 PM
#PRONTO INICIAMOS - GRACIAS POR LA ESPERA
#prestaciones de NumPy:
#1. Manejo de arreglos y matrices
#2. aritméticas, trigo, estad
#3. Indexación y "slicing" (acceder a subconjuntos de datos multidimensionales)
#4. Operaciones entre arreglos
#5. Eficiencia en manipulación de arreglos

lista_meses = [1,2,3,4,5,6,7,8,9,10,11,12]
lista_dias = list(range(1,366,1))
lista_ventas_mes = []
lista_ventas_dias_2021 = []
lista_ventas_dias_2022 = []

for i in range(0,12,1):
    lista_ventas_mes.append(r.random())

for i in range(0,365,1):
    lista_ventas_dias_2021.append(r.random()*1000000.0)
    lista_ventas_dias_2022.append(r.random()*1000000.0)

print(lista_ventas_mes)
print(lista_ventas_dias_2021)

#convertir de listas de python a arrays de numpy:
array_ventas_mes = np.array(lista_ventas_mes)
array_ventas_dias_2021 = np.array(lista_ventas_dias_2021)
array_ventas_dias_2022 = np.array(lista_ventas_dias_2022)

#suma de dos arreglos de 1 dimensión
array_ventas_2021_2022 = array_ventas_dias_2021 + array_ventas_dias_2022
lista_ventas_2021_2022 = lista_ventas_dias_2021 + lista_ventas_dias_2022 #¿?

#prueba de que las listas en python no se operan aritmeticamente como en álgebra lineal:

#operaciones aritméticas sobre vectores:
print( np.array([1,2,3,4])+np.array([5,6,7,8]))
print( np.array([1,2,3,4])-np.array([5,6,7,8]))
print(f"producto de vectores {np.array([1,2,3,4])*np.array([5,6,7,8])}") #producto elemento por elemento
#print(f"producto vectorial {np.cross(np.array([1,2,3]),np.array([2,2,2]))  }") #producto elemento por elemento
print(f"producto punto o escalar {np.dot(np.array([1,2,3]),np.array([2,2,2]))}") #producto elemento por elemento
print( np.array([1,2,3,4])/np.array([5,6,7,8]))

#parámetros estadísticos de datos desde numpy:

print(f"Media de los datos 2021:{np.mean(array_ventas_dias_2021)}"  )
print(f"Desviación Estándar datos 2021:{np.std(array_ventas_dias_2021)}"  )
print(f"Valor mínimo:{np.min(array_ventas_dias_2021)}"  )
print(f"Valor máximo:{np.max(array_ventas_dias_2021)}"  )


#--------------------- PANDAS, NUMPY Y MATPLOTLIB ------------------------------

#Uso de Pandas y NumPy:
datos_climaticos = {
    "meses":["enero","febrero","marzo","abril","mayo","junio"],
    "temp_prom_2021":[28.2,29.2,30.1,32.3,30.2,29.7],
    "temp_prom_2022":[29.2,30.5,31.3,33.7,30.5,28.9]
}

df_clima = pd.DataFrame(datos_climaticos)

temp_1 = 29.8
temp_2 = 30.3
dif_porc = ((temp_2 - temp_1)/temp_1) * 100
print(f"Diferencia porcentual de temperaturas:{dif_porc}")

temps_2021 = np.array(df_clima["temp_prom_2021"])
temps_2022 = np.array(df_clima["temp_prom_2022"])
cambio_porc = ((temps_2022 - temps_2021)/temps_2021)*100
print(f"Diferencias porcentuales meses:{cambio_porc}")



