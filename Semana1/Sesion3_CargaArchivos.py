#Talento TICs 2023 - Python 2 (python para analítica de datos)
# Sesión 3 - Carga de archivos (Noviembre 20)



#WORKFLOW DA:
# 1. CARGA DE DATOS -> 2. LIMPIEZA DE DATOS -> 3. ANÁLISIS -> 4. VISUALIZACIÓN 

#PARTE 1: CARGA DESDE ARCHIVOS PLANOS (CSV, JSON, XML, XLS,..)
#         (a) csv: comma separated values
#         (b) json: java script object notation
#         (c) xml: extended markup language
#         (d) xls: excel spreasheet
#         (e) sql: desde una base de datos sql

import pandas as pd

#Código para crear un diccionario de listas, a partir de un csv, con el que se puede
#construir un dataframe en Pandas:
def cargaArchivoPlano_Python(fileName):
    values = []
    meses = []
    temps = []
    with open(fileName) as file:    #modos de apertura de archivos de texto: r, lectura; w, escritura; a (append), agregar información al final
        for line in file:
            line = line.strip()     #remover espacios al inicio y al final de la cadena
            values = line.split(sep=";")                        #separar valores separados por coma
            print(values[0])
            print(values[1])
            meses.append(values[0])  #meses = ["Enero","Febrero",..."Junio"]
            temps.append(values[1])  #temp = [28.3,...,30.1]    
    
    dict = {"meses":meses,"temps": temps}
    return dict        


if __name__ == "__main__":

    #file_name = input("Cuál es la ruta del archivo plano?")

    #---------------  LEER UN CSV ----------------
    #cargar información de un archivo plano csv con una función propia:    
    #df_temps_manual = pd.DataFrame(cargaArchivoPlano_Python(file_name))
    #print(f"data set cargado manualmente:\n{df_temps_manual}")

    #cargar información de un archivo plano csv con pandas:
    # TENER EN CUENTA EL SEPARADOR DE LOS VALORES EN EL ARCHIVO
    # df_temps_pandas = pd.read_csv(file_name,sep=";")
    # print(f"Dataset cargado desde un csv con pandas:\n{df_temps_pandas}")


    #------------ LEER UN ARCHIVO JSON (JAVASCRIPT OBJECT NOTATION ) ------------
    # json_file = input("Cuál es la ruta del archivo JSON?")
    # df_temps_json = pd.read_json(json_file)
    # print(f"Dataframe cargado desde un archivo json:\n{df_temps_json}")

    #global education data
    #https://www.kaggle.com/datasets
    #https://www.kaggle.com/datasets/nelgiriyewithana/world-educational-data/
    df_global_edu_data = pd.read_csv("Global_Education.csv",sep=",")
    df_global_edu_data.info()








