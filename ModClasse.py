import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class CompTelefonica:
    def __init__(self,nome) :
        self.nome=nome
        #self.contr=False
        self.conv=False

    #1 CARICAMENTO ED ESPLORAZIONE INIZIALE  
    def leggi_csv(self):
        #self.contr=True
        self.df=pd.read_csv("ESERCIZIO ANALISI FUNZIONALE\\dataset_clienti.csv")
    
    def salva_csv(self):
        self.df.to_csv("ESERCIZIO ANALISI FUNZIONALE\\dataset_mod.csv")

    def stampa_csv(self):
        self.df=round(self.df,2)
        print(f"Il Dataset è:\n{self.df}")

    def statistiche(self):
        #prendo le statistiche del df e poi rinomino alcuni valori per essere comprensibili
        self.stats=self.df.describe()
        self.stats.rename(index={"50%":"Mediana"}, inplace=True)    #rinomina i valori
        self.stats.rename(index={"std":"Deviazione standard"}, inplace=True)
        self.stats.rename(index={"mean":"Media"}, inplace=True)
        self.stats.rename(index={"count":"Contatore"}, inplace=True)
        self.stats.rename(index={"min":"Minimo"}, inplace=True)
        self.stats.rename(index={"max":"Massimo"}, inplace=True)
        #arrotondo ogni valore a due cifre dopo la virgola
        self.stats=round(self.stats,2)
        print(f"Le statistiche sono:\n{self.stats}")

    def visualizza_eta(self):
        #visualizza diagramma eta
        sns.histplot(self.df['Età'], kde=True)
        plt.title('Distribuzione dei dati')
        plt.show()

    def visualizza_Durat_abb(self):
        sns.histplot(self.df['Durata_Abbonamento'], kde=True)
        plt.title('Distribuzione dei dati')
        plt.show()
    
    def vis_Servizio_Clienti_Contatti(self):
        sns.histplot(self.df['Servizio_Clienti_Contatti'], kde=True)
        plt.title('Distribuzione dei dati')
        plt.show()

    def vis_Tariffa_Mensile(self):
        sns.histplot(self.df['Tariffa_Mensile'], kde=True)
        plt.title('Distribuzione dei dati')
        plt.show()

    def vis_dati_cons(self):
        sns.histplot(self.df['Dati_Consumati'], kde=True)
        plt.title('Distribuzione dei dati')
        plt.show()

    def df_info(self):
        self.df.info()

    #esegue un print delle righe mancanti
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
        #se qualche riga è mancante:
        if len(self.df_righe_mancanti)>0:
            print("Opzioni:\n-->1. Riempire le righe mancanti con i valori medi delle altre righe\n-->2. Eliminare le righe")
            while True:
                scelta=input("Scelta: ")
                if scelta =="1":
                    for index in self.df_righe_mancanti.index:  #l'index rappresenta l'id
                        col_mancanti = self.df_righe_mancanti.loc[index].isnull() #verifica quale colonna è mancante dal df delle righe mancanti. Asseghna un booleano ad ogni colonna (False= ok) (true=valore mancante) 
                        col_mancanti = col_mancanti[col_mancanti].index.to_list()   #converte solo le colonne mancanti in una lista, cioè solo i valori true, andando a salvare il loro nome
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
        #verifca quale colonna ha numeri negativi
        self.eta_neg=self.df[self.df["Età"]<0]
        if len(self.eta_neg)>0:
            self.df["Età"] = self.df["Età"].abs()
            print(f"L'età dei clienti con id:",end=" ")  
            for index in self.eta_neg.index:
                print(index, end="")
            print(" è stata resa positiva")
            
        #verifca quale colonna ha numeri negativi
        self.abb=self.df[self.df["Durata_Abbonamento"]<0]
        if len(self.abb)>0:
            self.df["Durata_Abbonamento"]=self.df["Durata_Abbonamento"].abs()
        #verifca quale colonna ha numeri negativi
        self.dati=self.df[self.df["Dati_Consumati"]<0]
        if len(self.dati)>0:
            self.df=self.df["Dati_Consumati"].abs()
        #verifca quale colonna ha numeri negativi
        self.scc=self.df[self.df["Servizio_Clienti_Contatti"]<0]
        if len(self.scc)>0:
            self.df=self.df["Servizio_Clienti_Contatti"].abs()
        #verifca quale colonna ha numeri negativi
        self.tf=self.df[self.df["Tariffa_Mensile"]<0]
        if len(self.tf)>0:
            self.df=self.df["Tariffa_Mensile"].abs()
        
        #verifica le anomalie sulla colonna tariffe
        stats=self.df.describe()
        stats_cl=stats.loc[["75%"]]    #loc per selezionare la specifica riga del df "statistiche "che contiene il 75%
        tar_mens=stats_cl["Tariffa_Mensile"]
        self.tf=self.df[self.df["Tariffa_Mensile"]>(tar_mens.iloc[0]+15)]
        if len(self.tf)>0:
            print(f"75% Tariffe mensili: {tar_mens.iloc[0]}")
            print(f"Righe anomale sulle tariffe:\n{self.tf}")
            print("Riduzione automatica di 15 euro sulle tariffe.")
            #effettua una riduzione automatica delle tariffe anomale
            for index in self.tf.index:
                self.df.at[index, "Tariffa_Mensile"]-=15
                print("Riduzione effettuata")
        
        print(f"DataFrame aggiornato senza anomalie:\n{self.df}")

    def aggiungi_costo_gb(self):
        #aggiunge colonna costo/GB
        self.df["Costo_per_GB"]=self.df["Tariffa_Mensile"]/self.df["Dati_Consumati"]
        print(f"Colonna Costo/GB aggiunta:")
        self.stampa_csv()

    def eda(self):
        #converte i dati se non è già stato fatto
        if self.conv==False:
            self.converti_dati()
        #trova una correlazione tra queste colonne. Valore che oscilla tra -1 e 1
        self.correlazione= self.df[['Età', 'Durata_Abbonamento', "Tariffa_Mensile", "Churn"]].corr()
        self.correlazione["Churn"]=self.correlazione["Churn"].round().astype("int")
        self.correlazione=round(self.correlazione,2)
        print(f"Correlazione:\n{self.correlazione}")

    def converti_dati(self):
        #converte i dati
        self.df["Churn"]=self.df["Churn"].map(lambda x: 1 if x=="Sì" else 0)
        self.conv=True

    def normalizzazione(self):
        #trova tutte le colonna numeriche
        self.df_numerico = self.df.select_dtypes(include=[np.number])
        for col in self.df_numerico:
            if col=="ID_Cliente":
                continue
            nuova_col=col+"_norm"
            #crea una nuova colonna con valori normalizzati
            self.df[nuova_col]=(self.df[col] - self.df[col].min()) / (self.df[col].max() - self.df[col].min())
        print("Dataframe normalizzato:")
        self.stampa_csv()

#1 CARICAMENTO ED ESPLORAZIONE INIZIALE
#MENU
def menu():
    print("""\n---MENU'---
1. Stampa Dataframe
2. Aggiungi colonna costo/GB
3. Visualizza statistiche 
4. Visualizza informazioni sul dataframe
5. Gestisci valori mancanti
6. Elimina anomalie
7. Effettua un Analisi Esplorativa dei Dati
8. Aggiungi colonne normalizzate
9. Converti dati
10. Visualizza righe mancanti
11. Salva su un file.csv
12. Visualizza diagramma età
13. Visualizza diagramma durata abbonamento
14. Visualizza diagramma contatto servizio clienti
15. Visualizza Tariffe mensili
16. Visualizza diagramma dati consumati
17. Esci
""")