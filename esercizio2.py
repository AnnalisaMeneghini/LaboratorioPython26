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

#divido il testo in base al carattere \n = va a capo, individuo quindi le diverse righe 
lista_righe = testo.split('\n')

contatore=0
for riga in lista_righe:
    if len (riga) > 0:                    #tolgo quindi in questo modo le righe vuote 
        contatore = contatore + 1

print(contatore)


#conto le parole del testo in base al carattere ' ' 
lista_parole = testo.split()
#print(lista_parole)
conto = 0
for parola in lista_parole:
    if len (parola) > 0:
        conto = conto + 1 
print(conto)

testo_lista = list(testo)
print (testo_lista)


#carattere = 'a'

#alfanumerici = 'abcdef1234ABCD'
#carattere in alfanumerici 



for indice in [1,5,9,13]
    lista_parola_riga
