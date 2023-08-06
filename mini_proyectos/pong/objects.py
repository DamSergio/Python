import turtle

class Objetc:
    def __init__(self, x, y, color="white", speed=0):
        self.obj = turtle.Turtle()
        self.obj.speed(speed)
        self.obj.color(color)
        self.obj.penup()
        self.obj.goto(x, y)
        self.x = x
        self.y = y

    def reset(self):
        self.obj.goto(self.x, self.y)

    def get_x(self):
        return self.obj.xcor()
    
    def get_y(self):
        return self.obj.ycor()

class Panel(Objetc):
    def __init__(self, x, y, shape="square", color="white", speed=0):
        super().__init__(x, y, color, speed)
        self.obj.shape(shape)
        self.obj.shapesize(stretch_wid=5, stretch_len=1)
        self.points = 0
    
    def panel_up(self):
        y = self.obj.ycor()

        if y >= 250:
            return

        y += 20
        self.obj.sety(y)
    
    def panel_down(self):
        y = self.obj.ycor()

        if y <= -250:
            return

        y -= 20
        self.obj.sety(y)

class Ball(Objetc):
    def __init__(self, x, y, shape="square", color="white", speed=0, dx=1, dy=1):
        super().__init__(x, y, color, speed)
        self.obj.shape(shape)
        self.dx = dx
        self.dy = dy
    
    def move_x(self):
        self.obj.setx(self.obj.xcor() + self.dx)
    
    def move_y(self):
        self.obj.sety(self.obj.ycor() + self.dy)

class Lapiz(Objetc):
    def __init__(self, x=0, y=260, color="white", speed=0, player_a_points=0, player_b_points=0):
        super().__init__(x, y, color, speed)
        self.obj.hideturtle()
        self.obj.write(f"Player A: {player_a_points}  Player B: {player_b_points}", align="center", font=("Courier", 24, "normal"))
    
    def player_score(self, player_a_points, player_b_points):
        self.obj.clear()
        self.obj.write(f"Player A: {player_a_points}  Player B: {player_b_points}" ,align="center", font=("Courier", 24, "normal"))