import pandas as pd 
import numpy as np

eta= np.random.randint(18, 81, 300)
saldo_conto = np.random.uniform(0, 50000, 300)
numero_prodotti = np.random.randint(1, 6, 300)
anni_clienti = np.random.randint(0, 40, 300)
abbandonato = np.random.choice([0, 1], 300, p=[0.85, 0.15])
cliente_id = np.arange(1, 301)
print(eta)
print(saldo_conto)
print(numero_prodotti)
print(anni_clienti)
print(abbandonato)
df = pd.DataFrame({
    'cliente_id': cliente_id,
    'eta': eta,
    'saldo_conto': saldo_conto,
    'numero_prodotti': numero_prodotti,
    'anni_clienti': anni_clienti,
    'abbandonato': abbandonato
})

print(df.head())
df.to_csv("data/raw/clienti_banca.csv", index=False)