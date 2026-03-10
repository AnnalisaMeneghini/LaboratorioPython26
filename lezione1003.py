'''
import turtle

def disegna_quadrato(tartaruga, size, angolo):
   for i in range(4):
    tartaruga.forward(size)
    tartaruga.left(angolo)


def somma (a,b) :
  risultato = a + b
  return risultato
  
  ###################################################


result = somma(3,44)
print(result)
#print(a)


window = turtle.Screen()               # istanza "window" di Screen
window.bgcolor("lightgreen")           # imposto lo stato della "window"
# window.title("Raffaello & Donatello")

raffaello = turtle.Turtle()            # Istanza di Turtle chiamata raffaello
raffaello.color("red")                 # attributi per lo stato di raffaello    
raffaello.pensize(5)

disegna_quadrato(raffaello, 50, 90)

raffaello.right(180)                   # giro e sposto dall'origine raffaello
raffaello.forward(80)                  # 


donatello = turtle.Turtle()            # Istanza di Turtle chiamata donatello
donatello.color("violet")              # attributi per lo stato di donatello
donatello.pensize(7)

def disegna_triangolo(tartaruga, size):
  for i in range(3):
    tartaruga.forward(size)
    tartaruga.left(120)

#donatello.forward(80)                  # movimenti per disegnare un triangolo
#donatello.left(120)                    # con donatello
#donatello.forward(80)
#donatello.left(120)
#donatello.forward(80)
#donatello.left(120)               

disegna_quadrato(donatello, 100, 90)

disegna_triangolo(donatello, 150)

window.mainloop()                      # Attendo chiusura finestra di gioco o stop del programma

'''
import turtle
def koch(t, order, size):
    """
       La tartaruga t disegna frattale Koch di 'order' and 'size'
       lasciando la tartaruga nella direzioni iniziale
    """

    if order == 0:          
        # caso base che termina la ricorsione
        t.forward(size)
    else:
        # caso ricorsivo (ordine 1) in cui disegna i 4 segmenti
        koch(t, order-1, size/3)  
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        ##
        
        
window = turtle.Screen()               # istanza "window" di Screen
window.bgcolor("lightgreen")           # imposto lo stato della "window"
# window.title("Raffaello & Donatello")

raffaello = turtle.Turtle()            # Istanza di Turtle chiamata raffaello
raffaello.color("red")                 # attributi per lo stato di raffaello    
raffaello.pensize(5)

koch(raffaello, 3, 400)
window.mainloop()                      # Attendo chiusura finestra di gioco o stop del programma
