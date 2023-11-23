# PRACTICA WORKLOW ANÁLISIS DE DATOS
# QUÉ ES EL ANÁLISIS DE DATOS?
# PROCESO SISTEMÁTICO DE APLICAR TÉCNICAS DE CARGA, LIMPIEZA, ANÁLISIS ESTADÍSTICO DE DATOS
# EVALUAR Y APOYAR LA TOMA DE DECISIONES
#
#
# WORKFLOW DA:
# 1. CARGA DE DATOS -> 2. LIMPIEZA DE DATOS -> 3. ANÁLISIS -> 4. VISUALIZACIÓN 
#                               *
# (a)  determinar cuáles son los errores posibles / necesidades de análisis
#          ¿cuáles son las columnas importantes en la fase 3 del workflow?
#          identificar cuáles son los posibles errores presentes en esas columnas
#           -> formato de datos (numérico, real o entero, cadena de caracteres): astype
#           -> rango de datos (validación de acuerdo a los valores que se requieren)
#                 ej: edad de personas no admiten números negativos, rango de años, meses
#               iterar sobre el dataframe y analizar cada una de las columnas importantes
#
# (b)  determinar cómo se van a corregir
#           -> eliminación de filas con valores nulos:  dropna
#           -> eliminación de columnas nulas: drop
#           -> elminación de duplicados: drop_duplicated


# (1) cargar dataframe desde el archivo plano
#      datasets de prueba: 
#            https://github.com/dfloaizab/TalentoTIC2023/tree/main/Semana1/sampleDatasets/COVID clinical trials.csv
#            https://github.com/dfloaizab/TalentoTIC2023/blob/main/Semana1/sampleDatasets/police.csv        
# (2)  identificar los errores presentes, de acuerdo a su tipo
# (3)  corregirlos
