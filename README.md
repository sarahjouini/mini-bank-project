# Mini Bank Project – Analisi abbandono clienti (dataset sintetico)

Progetto di analisi dati su un dataset bancario sintetico, creato per esercitarmi sull'intero workflow di un Data Analyst: generazione dati, pulizia, analisi in Python e SQL, visualizzazione in Power BI.

## Domanda di business

I clienti che abbandonano la banca hanno caratteristiche diverse (saldo, numero di prodotti) rispetto a chi resta?

## Dataset

Dataset sintetico generato con Python (pandas e numpy), 300 clienti simulati con le seguenti colonne:
- `cliente_id`: identificativo cliente
- `eta`: età del cliente
- `saldo_conto`: saldo del conto in euro
- `numero_prodotti`: numero di prodotti bancari posseduti
- `anni_cliente`: anni di relazione con la banca
- `abbandonato`: 1 se il cliente ha abbandonato, 0 se è ancora cliente

Ho scelto un dataset sintetico perché i dati bancari reali sono riservati; genera la stessa logica di un dataset reale (variabili plausibili, target sbilanciato all'85%/15%, coerente con tassi di abbandono reali nel settore bancario).

## Struttura del progetto

```
mini-bank-project/
│
├── data/
│   ├── raw/              # dataset originale generato
│   └── processed/        # dataset pulito
│
├── scripts/
│   ├── 01_genera_dataset.py   # generazione dataset sintetico
│   └── 02_pulizia_eda.py      # pulizia dati ed EDA
│
├── sql/
│   └── analisi_mini_bank.sql  # query SQL di analisi
│
├── dashboard/
│   ├── mini_bank_dashboard.pbix
│   
│
└── README.md
```

## Cosa è stato fatto

**Generazione dataset (Python)**
- Creazione di 300 clienti simulati con numpy (età, saldo, numero prodotti, anni cliente, target abbandono con probabilità 85%/15%)

**Pulizia dati (Python)**
- Controllo duplicati su `cliente_id`
- Controllo valori mancanti
- Controllo tipi di dato

**EDA (Python)**
- Distribuzione del target `abbandonato`
- Confronto saldo medio tra clienti rimasti e abbandonati
- Confronto numero medio di prodotti tra clienti rimasti e abbandonati

**Analisi SQL**
- Conteggio clienti per stato di abbandono
- Saldo medio per stato di abbandono

**Dashboard Power BI**
- Grafico a barre: numero di clienti per stato di abbandono

<img width="197" height="139" alt="image" src="https://github.com/user-attachments/assets/53daca4a-96f8-4903-b3ec-9b00b5380d2b" />


## Strumenti utilizzati

Python (pandas, numpy) · SQL Server · Power BI · Git/GitHub

## Nota

Essendo i dati generati casualmente, le differenze osservate tra i gruppi (es. saldo medio) non rappresentano relazioni reali nei dati, ma il procedimento di analisi è lo stesso che si applicherebbe su un dataset reale.

## Autrice

**Sara Jouini** – [GitHub](https://github.com/sarahjouini)
