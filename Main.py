import ModClasse as mod

df=mod.CompTelefonica("Tim")
df.leggi_csv()
while True:
    mod.menu()
    scelta=input("Inserisci una scelta: ")
    if scelta=="1":
        try:
            df.stampa_csv()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")

    elif scelta=="2":
        try:
            df.aggiungi_costo_gb()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="3":
        try:
            df.statistiche()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="4":
        try:
            df.df_info()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="5":
        try:
            df.gestisci_val_manc()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="6":
        try:
            df.elimina_anomalie()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="7":
        try:
            df.eda()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="8":
        try:
            df.normalizzazione()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="9":
        try:
            df.converti_dati()
            print("Dati convertiti")
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="10":
        try:
            df.righe_mancanti()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")      
    elif scelta=="11":
        try:
            df.salva_csv()
            print("File salvato")
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="12":
        try:
            df.visualizza_eta()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="13":
        try:
            df.visualizza_Durat_abb()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="14":
        try:
            df.vis_Servizio_Clienti_Contatti()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="15":
        try:
            df.vis_Tariffa_Mensile()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="16":
        try:
            df.vis_dati_cons()
        except Exception as e:
            #Gestione errore
            print(f"Si è verificato un errore: {e}")
    elif scelta=="17":
        break
    else:
        print("Scelta sbagliata")

print("CHIUSURA PROGRAMMA")