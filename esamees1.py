# File: esamees1.py
#
# Author: Annalisa Meneghini
#
# Date: 30/06/2026
#
# Version: 1.0
#
# Description: es 1, lezione 3, funzioni

# 1. funzione che verifica se un numero è pari
def is_pari(n):
    """Ritorna vero se "n" è pari, se no ritorna falso """
    
    risultato = True

    if n%2 !=0 : 
        risultato = False
        
    return risultato

# 2. funzione chiede all'utente di inserire un numero intero positivo, lo verifica e lo restituisce : int svolge il ruolo da traduttore stringa-valore numerico 
def int_input():               #mettere la parentesi vuota perchè non richide di parametri in ingresso: interazione con utente--costruisco così un blocco riutilizzabile, se voglio riusare basta scivere x = int_input() 
    numero = int(input("Inserisci un numero intero positivo: "))       #"numero" è una etichetta 
    
    # Finché il numero è minore o uguale a zero, continua a chiederlo
    while numero <= 0:               #si entra nel ciclo se è minore o uguale a zero, sennò si va a return
        print("Valore non valido! Il numero deve essere maggiore di zero.")
        numero = int(input("Inserisci un numero intero positivo: "))      #nuovo input e aggiorna la variabile 'numero', poi valutare la condizione del while
        
    return numero


#
