


def generatore_tabellina(numero):
    """generatore infinito di multipli di un 'numero'"""
    n=0
    #loop infinito perchè non serve fermarmi al 10. loop finito con for 
    while(True):              #mi dice quanto dura
        yield n*numero
        n = n +1
################################## programma inizia da qui

num = input('con che numero desideri giocare?')   #num è una stringa, devo trasformarlo con un intero: con il castin, in caso posso mettere in questa riga davanti a tutto num
numero_intero=int(num)

print(f'giocheremo con il numero {numero_intero}')
g = generatore_tabellina(numero_intero)
numero_tabellina = next(g)


continua = True                 #metto varibile continua, uso una condizione potrei usare un loop infinito con il break
while continua:                  #è equivalente a scrivere  == True 
    
    guess = input(f'il numero attuale è {numero_tabellina}. Quale è il prossimo numero?')   #guess è una stringa

  #controllo se fermare il gioco 
    if guess == 'FINE' :
        continua = False       

    numero_tabellina = next(g)

    if numero tabellina == guess :         # ci sarà un porblmea di semantica, bisogna rifare
        print('hai indovinato!')
    else: 
        print('riprova')




    print(next(g))
    print(next(g))
    next(g)


print('esco dal gioco')              #avviene solo se la condizione qui dentro si verifica