import pandas as pd

class CompTelefonica:
    def __init__(self,nome) :
        self.nome=nome
        #self.contr=False
    
    def leggi_csv(self):
        #self.contr=True
        self.df=pd.read_csv("ESERCIZIO ANALISI FUNZIONALE\\dataset_clienti.csv")
    
    def stampa_csv(self):
        print(f"Il file csv è:\n{self.df}")

    def stats(self):
        self.stats=self.df.describe()
        self.stats=round(self.stats,2)
        print(f"Le statistiche sono:\n{self.stats}")
        
    def df_info(self):
        self.df.info()

    def righe_mancanti(self):
        self.righe_mancanti = self.df[self.df.isnull().any(axis=1)]
        if len(self.righe_mancanti)>0:
            print(f"Righe mancanti:\n{self.righe_mancanti}")
        else:
            print("Nessuna riga con valori mancanti")
#1 CARICAMENTO ED ESPLORAZIONE INIZIALE
df=CompTelefonica("Tim")
df.leggi_csv()
df.stampa_csv()
df.stats()
df.df_info()
df.righe_mancanti()