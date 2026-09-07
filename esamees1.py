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


# 3. funzione che generi lista se n pari, va diviso per 2 se dispari, va moltiplicato per 3 e aggiunto 1. continuo fino a 1 o lista + 100 numeri
def genera_sequenza(n):                      # n tra le arentesi a indicare che è necessario un parametro di ingresso 
    sequenza = [n]                           # [n] a indicare una lista: ad esempio se n vale 4 la variabile "sequenza" diventa la lista [4]
    
    while n != 1 and len(sequenza) < 100:    # il simbolo != diverso da 1 continua il ciclo while 
        if is_pari(n):
            n = n // 2
        else:                                # quando la condizione del if è falsa, cioè ho valori dispari 
            n = 3 * n + 1
            sequenza.append(n)               # appen(n) significa aggiungere in coda--allunga la lista preesistente, non creo una nuova lista
        
    return sequenza  

# 4. funzione che analizza la sequenza e restituisce massimo,lunghezza e somma della sequenza
def analizza_sequenza(lista):
    massimo = lista[0]                       # creo la variabile "massimo", prendo elemento in posizione 0 (la prima) provvisorio 
    somma = 0                                # sommo a 0 un numero (lo 0 non indice posizionale) 
    for numero in lista:                     # prendo uno alla volta un elemento della lista e lo chiamo "numero" e poi eseguo somma
        somma = somma + numero               
        if numero > massimo:                 # "if" all'intrno del for cioè controllo ogni elemento. se fosse fuori lo eseguirei una volta dopo che ciclo è terminato 
            massimo = numero                 # aggiorno il valore del massimo 
    lunghezza = len(lista)
    return massimo, lunghezza, somma


# 5. funzione che ricerca nella lista i valori divisibili per 5 e li manda a schermo
def ricerca(lista):
    trovati = False

    for numero in lista:                    #prendo in considerazione un numero alla volta 
        if numero % 5 == 0:                 # resto % della divisione per 5 è pari a 0, condizione vera e stampo
            print(numero)      
            trovati = True

    if trovati == False:                    # se non trovo nessun valore stampo 
        print("Non ci sono numeri divisibili per 5 nella sequenza")


# 6. 



