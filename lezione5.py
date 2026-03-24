import sys

#print('ciao' , sys.argv[2])

#print(sys.argv)

import argparse

#costruisce ed inizializza un oggetto ArgumentParser e lo assegna alla variabile parser
parser = argparse.ArgumentParser()


parser.add_argument('-n','--nome_esteso', help="E'il nome da stampare")
parser.add_argument('-b','--boolean_value', action='store_true', help="imposta il valore 'True' se trova il parametro")
parser.add_argument('-d','--con_default',  default='riferimento', help="Parametro che ha già un valore di default se non viene fornito l'argomento")

variabili = parser.parse_args()   

print(variabili.nome_esteso)

