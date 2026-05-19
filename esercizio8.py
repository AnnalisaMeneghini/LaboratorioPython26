#ESERCIZIO 8
#autore: Annalisa Meneghini
#data: 19.05
#fatto con gemini 



def gioco_impiccato(parola_segreta):               #statement della funzione: solo 1 in cui definiamo la funzione
    ''' documentazione su cosa fa la funzione'''
    # Trasformiamo la parola in maiuscolo per evitare problemi di maiuscole/minuscole
    parola_segreta = parola_segreta.upper()        #se inserisco lettera maiuscola mi da errore 
    
    # Set per memorizzare le lettere inserite dall'utente
    lettere_indovinate = set()
    lettere_sbagliate = set()
    
    # Numero massimo di errori consentiti
    tentativi_rimasti = 6
    
    print("--- BENVENUTO AL GIOCO DELL'IMPICCATO! ---")
    
    while tentativi_rimasti > 0:
        # 1. Mostra lo stato attuale della parola (es. STR_NG_)
        parola_visualizzata = []
        for lettera in parola_segreta:
            if lettera in lettere_indovinate:
                parola_visualizzata.append(lettera)
            else:
                parola_visualizzata.append("_")
        
        parola_corrente = " ".join(parola_visualizzata)
        print(f"\nParola da indovinare: {parola_corrente}")
        print(f"Lettere sbagliate: {', '.join(sorted(lettere_sbagliate))}")
        print(f"Tentativi rimasti: {tentativi_rimasti}")
        
        # Controllo vittoria: se non ci sono più trattini, l'utente ha vinto
        if "_" not in parola_visualizzata:
            print(f"\n🎉 Complimenti! Hai indovinato la parola: {parola_segreta}")
            return True
            
        # 2. Input dell'utente con controllo validità
        tentativo = input("Inserisci una lettera: ").upper().strip()
        
        if len(tentativo) != 1 or not tentativo.isalpha():
            print("Per favore, inserisci una sola lettera valida.")
            continue
            
        if tentativo in lettere_indovinate or tentativo in lettere_sbagliate:
            print("Hai già provato questa lettera!")
            continue
            
        # 3. Verifica se la lettera è corretta o meno
        if tentativo in parola_segreta:
            print(f"Ottimo! La lettera '{tentativo}' è presente.")
            lettere_indovinate.add(tentativo)
        else:
            print(f"Peccato! La lettera '{tentativo}' non c'è.")
            lettere_sbagliate.add(tentativo)
            tentativi_rimasti -= 1
            
    # Se il ciclo finisce senza un return, i tentativi sono esauriti (Sconfitta)
    print(f"\n💥 Game Over! Hai esaurito i tentativi. La parola era: {parola_segreta}")
    return False

# Esempio di utilizzo:
# Puoi avviare il gioco passando la parola che desideri

gioco_impiccato("felicia")          #la chiamo per avere un risultato, qui inizia il programma
           