import turtle #modulo para graficos simples
import time
from objects import Panel, Ball, Lapiz

window = turtle.Screen() #pantalla
window.title("Pong game") #titulo
window.bgcolor("black") #color de fondo
window.setup(width=800, height=600) #tamaño de la pantalla
window.tracer(0) #velocidad que se actualiza la pantalla (0 es que no se actualiza)

#panel A
panel_a = Panel(-350, 0)
window.listen()
window.onkeypress(panel_a.panel_up, "w") #no poner los parentesis en la funcion IMPORTANTE
window.onkeypress(panel_a.panel_down, "s")
#panel B
panel_b = Panel(350, 0)
window.onkeypress(panel_b.panel_up, "Up")
window.onkeypress(panel_b.panel_down, "Down")
#bola
ball = Ball(0, 0)

#Lapiz
score = Lapiz()

#Main game loop
while True:
    restart = False
    window.update() #actualiza la pantalla

    ball.move_x()
    ball.move_y()

    if ball.get_y() >= 290:
        ball.dy = -1
    
    if ball.get_y() <= -290:
        ball.dy = 1
    
    if ball.get_x() >= 340 and panel_b.get_y() in range(int(ball.get_y()) - 50, int(ball.get_y()) + 51):
        ball.dx = -1
    
    if ball.get_x() <= -340 and panel_a.get_y() in range(int(ball.get_y()) - 50, int(ball.get_y()) + 51):
        ball.dx = 1
    
    if ball.get_x() <= -360:
        panel_b.points += 1
        score.player_score(panel_a.points, panel_b.points)
        restart = True
    
    if ball.get_x() >= 360:
        panel_a.points += 1
        score.player_score(panel_a.points, panel_b.points)
        restart = True
    
    if panel_a.points == 10 or panel_b.points == 10:
        window.update() #actualiza la pantalla
        break
    
    if restart:
        panel_a.reset()
        panel_b.reset()
        ball.reset()
    
    time.sleep(0.005)

turtle.done()