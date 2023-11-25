import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df_global_ed = pd.read_csv("Global_Education.csv")
df_global_ed.info()
df_global_ed = df_global_ed.apply(lambda x: pd.factorize(x)[0] )
df_sub = df_global_ed[  ["Countries and areas","Birth_Rate","Unemployment_Rate","Primary_End_Proficiency_Math","Primary_End_Proficiency_Reading" ]]

#df_sub.rename(columns={"Countries and areas":"C/A","Birth_Rate":"Nat","Primary_End_Proficiency_Math":"Mat","Primary_End_Proficiency_Reading":"Lectura"},inplace=True)

corr = df_sub.corr()
df_sub.plot.hist(x="Countries and areas",y="Birth_Rate") 
plt.show()

#Visualización de la correlación como un mapa de calor (usando la librería seaborn)
plt.figure(figsize=(10,10))
sb.heatmap(corr, annot=True, cmap="coolwarm",fmt=".2f",linewidths=.5)
plt.title("Matriz de Correlación")
plt.show()
