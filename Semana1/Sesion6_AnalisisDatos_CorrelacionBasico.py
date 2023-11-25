import pandas as pd
df_global_ed = pd.read_csv("Global_Education.csv")

df_global_ed.info()

df_global_ed = df_global_ed.apply(lambda x: pd.factorize(x)[0] )

df_sub = df_global_ed[  ["Countries and areas","Birth_Rate","Unemployment_Rate","Primary_End_Proficiency_Math","Primary_End_Proficiency_Reading" ]]

df_sub.rename(columns={"Countries and areas":"C/A","Birth_Rate":"Nat","Primary_End_Proficiency_Math":"Mat","Primary_End_Proficiency_Reading":"Lectura"},inplace=True)

print(df_sub.corr())
