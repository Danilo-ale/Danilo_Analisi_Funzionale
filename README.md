# Danilo_Analisi_Funzionale
Esercizio finale Pandas.
ESERCIZIO:
1.Caricamento e Esplorazione Iniziale:
    1.1 Caricare i dati da un file CSV.
    1.2 Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con
    valori mancanti.
2Pulizia dei Dati:
    2.1 Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
    2.2 Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).
3.Analisi Esplorativa dei Dati (EDA):
    3.1 Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
    3.2 Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
    3.3 Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.
4.Preparazione dei Dati per la Modellazione:
    4.1 Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
    4.2 Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.
5.Analisi Statistica e Predittiva:
    5.1 Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
        su altri fattori.
    5.2 Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve).

ANALISI FUNZIONALE ESERCIZIO

---OBIETTIVO---
Creare un programma che gestisca i dati dei clienti e calcoli il churn rate.
Creare un modello predittivo e scoprire correlazioni tra i dati

---REQUISITI PROGRAMMA---
--> Carimento dati: il programma deve essere in grado di caricare i dati da un file.csv, dal quale
bisogna effettuare una prima analisi di rilevamento dati e valori mancanti
        Tempo stimato: 15/20 minuti
--> Pulizia dati: il programma deve gestire eventuali dati mancanti. Attraverso dei 
controlli bisogna verificare che i dati abbiano senso (età, durata abbonamento, Dati consumati non negativi ecc..)
        Tempo stimato: 25/30 minuti
--> Analisi esplorativa dei dati: creazione nuove colonne utili per analisi (es. Costo/GB)
Verificare correlazioni tra età, durata abbonamento, tariffe mensili e churn.
        Tempo stimato: 40/50 minuti
--> Preparazione dati per la modellazione: conversione dati per essere pronti alla 
modellazione.
        Tempo stimato: 20/25 minuti

--> Analisi statistica e Predittiva: fondamentale esplorazione di librerie appropriate. Tempo stimato: 20/25 minuti
Tempo di esecuzione variabile della task: variabile. >40 minuti

--> TEMPO VARIABILE PER DEBUG: Tempo extra per verifica funzionamento totale
del programma
        Tempo stimato: 25/30 MINUTI

--> REQUISITI FUNZIONALI: creazione del menù in un modulo separato. Effettuare 
appropriati controlli per evitare errori improvvisi.
        Tempo stimato: 20 minuti
