import pandas as pd
df = pd.read_csv("data/raw/clienti_banca.csv")
print(df.head())
print(df['cliente_id'].duplicated().sum())
print(df.isnull().sum())
print(df.info())