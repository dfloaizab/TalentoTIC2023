#Talento TICs 2023
#Python 2

#Relacionando dos datasets
import pandas as pd
import matplotlib.pyplot as plt

#concatenación y merge de datasets:

#
sales_data_pts = {
    "point_id": [1,2,3,4,5,6,7,8],
    "nombres": ["Centro","Sur","Norte","Oriente","Occidente","Sur 2","Norte 2","Centro 2"],
    "sales_pt" : [  100.0, 200.00, 300.00,150.00,400.00,90.00,120.00,88.00 ]
}

sales_data_prod = {
    "point_id": [1,2,3,4,5,6,7,8],
    "prod_id": [11,12,13,11,21,11,30,21],
    "prod": ["Zapatos A","Zapatos B","Zapatos C","Zapatos D","Zapatos E","Zapatos F","Zapatos G","Zapatos H"],
    "sls_prd" : [  20.0, 15.00, 10.00,12.00,9.00,11.00,22.00,18.5 ]
}

df_sales_pt = pd.DataFrame(sales_data_pts)
df_sales_prod = pd.DataFrame(sales_data_prod)

print(df_sales_pt)
print(df_sales_prod)

#el merge, mezcla dos datasets/dataframes con distintas columnas, a partir de una columna común
#no importa que tengan distinto # de filas
df_all_data = pd.merge(df_sales_pt, df_sales_prod,on="point_id")

#podemos operar con el nuevo dataset de acuerdo a lo visto hasta ahora:
df_group = df_all_data.groupby("prod")["sls_prd"].sum().plot(kind="bar")
plt.show()
print(df_group)






