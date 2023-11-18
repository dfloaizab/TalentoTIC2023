#Repaso de manejo de datos en Python (colecciones)
#https://github.com/dfloaizab/TalentoTIC2023/tree/main/Semana1

#1. sintáxis
#2. Multiplataforma / multipropósito (seguridad informática, desarrollo, IA, automatización)
#3. Multiparadigma (?) - Modelo de solución de problemas:
#                        * estructurado (ciclos, condicionales, funciones)  
#                        * orientado a objetos (clases, objetos)                      
#                        * funcional (las funciones son "ciudadanos de primer orden"):
#                        *      funciones pueden ser usadas como objetos
#4. interprete ligero (microPython)
#5. librerias
#6. dinámicamente tipado (?) - tipo de dato, se infiere en tiempo de ejecución

nombre = "Diego" #cadena de caracteres
edad = 46        #entero
fuma = False     #booleano 
peso = 58.9      #float
estatura = 1.60

#las listas en python pueden almacenar objetos de distinto tipo:
mascotas = ["Falkor","Sabina", "Kira"]
info_diego = [nombre, edad, fuma, peso, estatura, mascotas]

for elemento in info_diego:
    print(type(elemento))

print(info_diego)

#colecciones de datos:
# listas, diccionarios, tuplas, conjuntos

#Carrito de compras:
# lista de productos, cada producto tiene precio, inventario:
#      - codigo
#      - nombre
#      - valor unitario
#      - inventario
# 1. ¿dónde almacenar la información?
 
 #diccionario para definir información de un producto (1 registro):
producto1 = {"id": 1, "nombre": "Zapatillas Converse", "precio_u":250000.0, "inv":50}
producto2 = {"id": 2, "nombre": "Zapatillas Nike", "precio_u":350000.0, "inv":25}
producto3 = {"id": 3, "nombre": "Zapatillas Adidas", "precio_u":380000.0, "inv":30}
producto4 = {"id": 4, "nombre": "Zapatillas Diesel", "precio_u":500000.0, "inv":15}

# "dataset" como una lista de diccionarios:
lista_productos_2 = [
    {"id": 1, "nombre": "Zapatillas Converse", "precio_u":250000.0, "inv":50},
    {"id": 2, "nombre": "Zapatillas Nike", "precio_u":350000.0, "inv":25},
    {"id": 3, "nombre": "Zapatillas Adidas", "precio_u":380000.0, "inv":30},
    {"id": 4, "nombre": "Zapatillas Diesel", "precio_u":500000.0, "inv":15}
]

#una lista de objetos diccionario:
lista_productos = [producto1, producto2]

#operaciones sobre diccionarios:
#obtener valor de determinada clave/llave
print(producto1["id"])
print(producto2["inv"])

#operaciones sobre listas:
#a. indexar elemento:
print(lista_productos[0])
#b. agregar elemento a la lista:
lista_productos.append(producto3) #agrega al final
lista_productos.insert(1,producto4) #agrega en cualquier posición
print(lista_productos)

#ITERACION SOBRE COLECCIONES DE DATOS

#iteración sobre diccionarios:
print("llaves/valor de diccionario producto 1:")
for key in producto1:
    print(f"llave: {key}, valor: {producto1[key]}")

#iteracion sobre listas / diccionarios:
#observacion: tener en cuenta el tipo de elemento sobre el cual se está iterando:
for record in lista_productos:
    print(f"Registro: {record['id']}, {record}")
    for key in record:
        print(record[key]) #inprime el valor que corresponde a la llave de cada registro:


#FILTRADO DE ELEMENTOS EN COLECCIONES DE OBJETOS
#filtrado de elementos en listas

#usando funciones de filtrado:
#defino una función booleana (que devuelve True o False) sobre un parámetro
def es_par(n):
    return n%2 == 0

print(f"es par? {es_par(254874)}")

#1. usando la función de alto orden*: "filter"
#* una función de alto orden es una función que puede ser usada como parámetro de otra función, o recibir una
#  función como parámetro
lista_numeros = list(range(1,101,1)) #range, genera una iteración de números desde 1, hasta 100, con incrementos de 1
#la función "filter" aplica la función que se recibe como primer parámetro sobre la colección de datos
#del segundo parámetro, generando una nueva lista

lista_pares_ciclo = []

#filtrar con un ciclo:
for num in lista_numeros:
    if es_par(num):
        lista_pares_ciclo.append(num)

#filtrar usando la función "filter"
lista_filtrada = list(filter( es_par, lista_numeros))

print(lista_numeros)
print(f"lista filtrada:{lista_filtrada}")
print(f"lista filtrada con un ciclo:{lista_pares_ciclo}")

#usando una función "lambda" (característica del paradigma funcional):
# lambda es la palabra usada para la abstracción "función"

# n es el parámetro
# n%2 == 0 es el retorno de la función
fun_es_par = lambda n: n%2 == 0
#aquí se define directamente la función que será usada como filtro como una función lambda, anónima
lista_filtrada_v3 = list(filter( lambda n: n%2 == 0 ,lista_numeros   ))

print(fun_es_par(654654))

#ejercicio 1: uso de función filter y funciones lambda
#filtre la lista de números para los múltiplos de 3:



#usando "list comprehension":



#repaso de operaciones con datos y colecciones de datos en Python
