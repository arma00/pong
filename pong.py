import turtle

wn = turtle.Screen()
wn.setup(width = 800, height = 600)
wn.bgcolor("black")
wn.tracer(0)

# Score
score1 = 0
score2 = 0
won = False

# Player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("turtle")
player1.color("blue")
player1.penup()
player1.goto(-350, 0)


# Player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("turtle")
player2.color("orange")
player2.penup()
player2.goto(350, 0)


# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.dot(5,"white")
# ball.shape("circle")
# ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2


# Function
def player1_up():
  y = player1.ycor()
  y += 20 # Adds 2 pixels to y-coord
  player1.sety(y)

def player1_down():
  y = player1.ycor()
  y -= 20
  player1.sety(y)

def player2_up():
  y = player2.ycor()
  y += 20 # Adds 2 pixels to y-coord
  player2.sety(y)

def player2_down():
  y = player2.ycor()
  y -= 20
  player2.sety(y)

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align = "center", font=("Courier", 24, "normal"))

# Keyboard binding
wn.listen() # listen for keyboard input
wn.onkey(player1_up,"w") # when user presses "w" on keyboard call function player1_up
wn.onkey(player1_down, "s")
wn.onkey(player2_up,"Up") 
wn.onkey(player2_down, "Down")


# Main game loop
while True:
  wn.update()

  if won:
    break

  # Move the ball
  ball.clear()
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)
  ball.dot(5,"white")

  # Border checking
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1 # reverses direction
  
  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390:
    ball.goto(0)
    ball.dx *= -1
    score1 += 1
    pen.clear()
    pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align = "center", font=("Courier", 24, "normal"))

  
  if ball.xcor() < -390:
    ball.goto(0,0)
    ball.dx *= -1
    score2 += 1
    pen.clear()
    pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align = "center", font=("Courier", 24, "normal"))

  # Paddle and ball collisions
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
    ball.setx(340)
    ball.dx *= -1

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
    ball.setx(-340)
    ball.dx *= -1


  if score1 == 3:
    pen.clear()
    pen.write("Player 1 Wins!", align = "center", font=("Courier", 24, "normal"))
    won = True
  elif score2 == 3:
    pen.clear()
    pen.write("Player 2 Wins!", align = "center", font=("Courier", 24, "normal"))
    won = True

