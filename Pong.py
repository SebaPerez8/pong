import turtle  
import winsound


ventana = turtle.Screen()
ventana.title("PONG")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)  
ventana.tracer(0)

# Score
score_a = 0
score_b = 0

# Paleta A
paleta_a = turtle.Turtle()
paleta_a.speed(0)
paleta_a.shape("square") 
paleta_a.color("white")
paleta_a.shapesize(stretch_wid=5, stretch_len=1) 
paleta_a.penup() 
paleta_a.goto(-350, 0)  

# Paleta B
paleta_b = turtle.Turtle()
paleta_b.speed(0)
paleta_b.shape("square") 
paleta_b.color("white")
paleta_b.shapesize(stretch_wid=5, stretch_len=1) 
paleta_b.penup() 
paleta_b.goto(350, 0)  

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square") 
bola.color("white")
bola.penup() 
bola.goto(0, 0)  
bola.dx = 0.3
bola.dy = -0.3

# Lapiz
lapiz = turtle.Turtle()
lapiz.speed(0)
lapiz.color("white")
lapiz.penup()
lapiz.hideturtle()
lapiz.goto(0, 260)
lapiz.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 24, "normal"))

# Funcion 
def paleta_a_sube():
    y = paleta_a.ycor()
    y += 20
    paleta_a.sety(y)

def paleta_a_baja():
    y = paleta_a.ycor()
    y -= 20
    paleta_a.sety(y)

def paleta_b_sube():
    y = paleta_b.ycor()
    y += 20
    paleta_b.sety(y)

def paleta_b_baja():
    y = paleta_b.ycor()
    y -= 20
    paleta_b.sety(y)

# Keyboard binding
ventana.listen()
ventana.onkeypress(paleta_a_sube, "w")  
ventana.onkeypress(paleta_a_baja, "s")   
ventana.onkeypress(paleta_b_sube, "Up")  
ventana.onkeypress(paleta_b_baja, "Down")   

# Main game loop
while True:
    ventana.update()

    # Movimiento de bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Border checking
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)   

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_a += 1
        lapiz.clear()
        lapiz.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        paleta_b.goto(350, 0)
        paleta_a.goto(-350, 0)

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_b += 1  
        lapiz.clear()
        lapiz.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))  
        paleta_b.goto(350, 0)
        paleta_a.goto(-350, 0)

    # Choque de paleta y bola
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < paleta_b.ycor() + 40 and bola.ycor() > paleta_b.ycor() -40):
        bola.setx(340)
        bola.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < paleta_a.ycor() + 40 and bola.ycor() > paleta_a.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1   
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) 
