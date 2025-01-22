import turtle
import random
 
larg = 700
alt  = 500
bacca_lato = 10
ritardo = 100 #tempo per aggiornare la pagina
 
spostamenti = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset():
   
    global snake, snake_dir, bacca_pos,sas1_pos, sas2_pos, sas3_pos, pen
    #global fa sì che i valori attribuiti alle variabili in questione siano validi anche fuori dalla funzione
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
  # l'ultima lista rappresenta la testa
    snake_dir = "up"
  
    bacca_pos = bacca_random()
    bacca.goto(bacca_pos)
  
    sas1_pos = bacca_random()
    sasso1.goto(sas1_pos)
    sas2_pos = bacca_random()
    sasso2.goto(sas2_pos)
    sas3_pos = bacca_random()
    sasso3.goto(sas3_pos)
  
    move_snake()
  #questa funzione senza argomento verrà implementata alla fine
     
def move_snake():
    global snake_dir
 
    new_head = snake[-1].copy()
  #in verità i valori attribuiti a new_head non sono questi; l'importante era stabilire la dimensione corretta
    new_head[0] = snake[-1][0] + spostamenti[snake_dir][0]

    new_head[1] = snake[-1][1] + spostamenti[snake_dir][1]
  #in funzione della direzione del serpente, modifica la "testa"
          
    if scontro() or new_head in snake[:-1] : 
      reset()
    #ricomincia il gioco; significa che il giocatore ha perso quindi riavvia
    else:
        snake.append(new_head)
        if not mangio():
            snake.pop(0)
        #ciò fa sì che il serpente si allunghi solo se ha effettivamente mangiato la bacca
 
        if snake[-1][0] > larg/ 2:
            snake[-1][0] -= larg
        elif snake[-1][0] < - larg/ 2:
            snake[-1][0] += larg
        elif snake[-1][1] > alt / 2:
            snake[-1][1] -= alt
        elif snake[-1][1] < -alt / 2:
            snake[-1][1] += alt
 #ciò si traduce nell'effetto "Pacman"
 
        pen.clearstamps()
 #cancella le parti del serpente, ristampandone di nuove e con posizioni diverse nel prossimo punto, garantendo uno spostamento del serpente dopo l'update della finestra
         
        for segmento in snake:
            pen.goto(segmento[0], segmento[1])
            pen.stamp() #questo è ciò che fornisce il "corpo" del serpente
   
        finestra.update()
 
        turtle.ontimer(move_snake, ritardo) #attiva la funzione "move_snake" dopo il tempo "ritardo", espresso inn millisecondi
 
def mangio():
    global bacca_pos
    if dist(snake[-1], bacca_pos) < 20:
        bacca_pos = bacca_random()
        bacca.goto(bacca_pos) #cambia la posizione della bacca appena l'ha mangiata
        return True
    return False

def scontro():

    if dist(snake[-1], sas1_pos) < 20 or  dist(snake[-1], sas2_pos) < 20 or dist(snake[-1], sas3_pos) < 20 :
      return True
    return False
#indica la collisione con le rocce
  
def bacca_random():
    x = random.randint(- larg/ 2 + bacca_lato, larg/ 2 - bacca_lato)
    y = random.randint(- alt/ 2 + bacca_lato, alt/ 2 - bacca_lato)
    return (x, y)
  #restituisce due coordinate per una posizione a caso

def dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    res = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return res #restitisce la distanza fra due punti

def go_up():#dirige il serpente verso l'alto
    global snake_dir
    if snake_dir != "down": #nota che proprio grazie a questo != una volta fissata la direzione e il verso, la biscia non può muoversi nel verso opposto
        snake_dir = "up"
 
def go_right():#dirige il serpente verso destra
    global snake_dir
    if snake_dir != "left":
        snake_dir = "right"
 
def go_down():#dirige il serpente verso il basso
    global snake_dir
    if snake_dir!= "up":
        snake_dir = "down"
 
def go_left():#dirige il serpente verso sinistra
    global snake_dir
    if snake_dir != "right":
        snake_dir = "left"
 
 
finestra = turtle.Screen()
finestra.setup(larg, alt)
finestra.title("Snake")
finestra.bgcolor("green")
finestra.tracer(0)
#Ponendo tracer(0), gli aggiornamenti automatici dello schermo sono disattivati. Quindi è necessario chiamare in modo esplicito "update()" quando si vuole far sì che lo schermo rifletta lo stato corrente del disegno.
 
 
pen = turtle.Turtle("square")
pen.up()
#ponendo pen.up() si può togliere lo "striscione" lasciato dalla biscia
 
#definisco la bacca come oggetto
bacca = turtle.Turtle()
bacca.shape("triangle")
bacca.color("light green")
bacca.shapesize(bacca_lato / 15)
bacca.penup()

#creo una nuova forma per gli ostacoli, più simile alla forma nel gioco originale
shape =((0, 0), (10, 10), (20, 0), (10, -10))
turtle.register_shape('rombo', shape)

#definisco le rocce come oggetti
sasso1=turtle.Turtle()
sasso1.shape('rombo')
sasso1.color("navy blue")
sasso1.shapesize(bacca_lato / 10)
sasso1.penup()


sasso2=turtle.Turtle()
sasso2.shape('rombo')
sasso2.color("navy blue")
sasso2.shapesize(bacca_lato / 10)
sasso2.penup()


sasso3=turtle.Turtle()
sasso3.shape('rombo')
sasso3.color("navy blue")
sasso3.shapesize(bacca_lato / 10)
sasso3.penup()


 
finestra.listen() #rende la finestra "ricettiva" a input sullo schermo
finestra.onkey(go_up, "Up")#significa che premendo sulla tastiera il tasto Up si "attiva" la funzione go_up()
finestra.onkey(go_right, "Right")
finestra.onkey(go_down, "Down")
finestra.onkey(go_left, "Left")


reset()

turtle.mainloop()
