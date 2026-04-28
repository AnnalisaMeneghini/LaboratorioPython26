testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

#risolvo la prima parte dell'esercizio

#divido il testo in base al carattere \n = va a capo, individuo quindi le diverse righe, 1
lista_righe = testo.split('\n')

contatore=0
for riga in lista_righe:
    if len (riga) > 0:                    #tolgo quindi in questo modo le righe vuote 
        contatore = contatore + 1

print(contatore)


#conto le parole del testo in base al carattere ' ' 2
lista_parole = testo.split()
#print(lista_parole)
conto = 0
for parola in lista_parole:
    if len (parola) > 0:
        conto = conto + 1 
print(conto)

#testo_lista = list(testo)
#print (testo_lista)

#TERZO PUNTO ESERCIZIO : isalnum che in caso posso utilizzare
#carattere = 'a'            #mi fa scorrere la lista di caratteri alfanumerici
alfanumerici = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lista_alfanumerici = testo.split()
count = 0 

for carattere in testo:
    if carattere in alfanumerici:
        print (carattere)     #per controllare che effettivemente torni, mi stampa caratteri tranne accenti, sapazi virgole: verifica
        count = count + 1 
print (count) 

#QUARTO PUNTO ESERCIZIO: 
n = str(input("inserisci una lettera: \n"))          #n è una variabile che assumerà il valore della lettera \n per andare a capo, una questione di bellezza
count = 0

for x in testo: #scorro il testo carattere per carattere, x cambia valore in ogni lettera: ciao x prima è c poi i poi a etc
    if (x == n): 
        count = count + 1

print(f"La lettera compare {count} volte nel testo")

###for indice in [1,5,9,13]
    ##lista_parola_riga
