import pandas as pd

class CompTelefonica:
    def __init__(self,nome) :
        self.nome=nome
        #self.contr=False

    #1 CARICAMENTO ED ESPLORAZIONE INIZIALE  
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
        self.contr_df_righe=True
        self.df_righe_mancanti = self.df[self.df.isnull().any(axis=1)]
        if len(self.df_righe_mancanti)>0:
            print(f"Righe mancanti:\n{self.df_righe_mancanti}")
        else:
            print("Nessuna riga con valori mancanti")         

    #2 PULIZIA DEI DATI
    def gestisci_val_manc(self):
        self.righe_mancanti()
        if len(self.df_righe_mancanti)>0:
            print("Opzioni:\n-->1. Riempire le righe mancanti con i valori medi delle altre righe\n--->2.Eliminare le righe")
            while True:
                scelta=input("Scelta: ")
                if scelta =="1":
                    for index in self.df_righe_mancanti.index:  #l'index rappresenta l'id
                        col_mancanti = self.df_righe_mancanti.loc[index].isnull() #verifica quale colonna è mancante dal df delle righe mancanti. Asseghna un booleano ad ogni colonna (False= ok) (true=valore mancante) 
                        print("ok", col_mancanti)      
                        col_mancanti = col_mancanti[col_mancanti].index.to_list()   #converte solo le colonne mancanti in una lista, cioè solo i valori true, andando a salvare il loro nome
                        print("gist", col_mancanti)   
                        print(f"Riga: {index} Colonne mancanti: {col_mancanti}")
                        for col in col_mancanti:        #per ogni colonna della lista, la riempie con il valore medio dell"nintera colonna
                            self.df.fillna({col: self.df[col].mean()}, inplace=True)
                    
                    print("Colonne riempite con i valori medi delle altre righe!")
                    break
                elif scelta=="2":   #elimino dal df tutte le righe che sono presenti anche nel df_righe_mancanti
                        self.df=self.df.drop(self.df_righe_mancanti.index)
                        print("Righe eliminate.")
                        print(self.df)
                        break
                else:
                    print("Scelta sbagliata")

    def elimina_anomalie(self):
        self.df=self.df[self.df["Età"] > 0]
        self.df=self.df[self.df["Durata_Abbonamento"] > 0]
        self.df=self.df[self.df["Dati_Consumati"] > 0]
        self.df=self.df[self.df["Servizio_Clienti_Contatti"] > 0]
        self.df=self.df[self.df["Tariffa_Mensile"] > 0]
        print(f"DataFrame aggiornato senza anomalie:\n{self.df}")


#1 CARICAMENTO ED ESPLORAZIONE INIZIALE
df=CompTelefonica("Tim")
df.leggi_csv()
df.stampa_csv()
#df.stats()
#df.df_info()
#df.gestisci_val_manc()
df.correggi_anomalie()


