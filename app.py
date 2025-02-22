import pandas as pd

#Ejercicio 0.0
# ds = pd.read_csv('assets/real_estate.csv', sep=';')
# print(ds)
#Ejercicio 1
# df = pd.read_csv('assets/real_estate.csv')
#Ejercicio 2
import pandas as pd
df = pd.read_csv('assets/real_estate.csv')
teuer = df.loc[df['price'].idxmax()]
print(teuer)
