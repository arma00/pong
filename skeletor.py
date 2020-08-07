import turtle

# set up screen
wn = turtle.Screen()
# make the screen 600 x 800 pixels
# set the screen's background color

# Score
score1 = 0
score2 = 0


# Player 1
# set the player's speed, shape, color
player1 = turtle.Turtle()
player1.goto(-350, 0) # set the player's initial position


# Player 2
# set the player's speed, shape, color
player2 = turtle.Turtle()
player2.goto(350, 0) # set the player's initial position


# Ball 
# make the ball a white .dot() with radius 5
# set its speed to 0
# set its direction of movement to be over 2 and up 2
ball = turtle.Turtle()


# Functions!
def player1_up():
  # Adds 2 pixels to y-coord
  return
  
def player1_down():
  # Subtracts 2 pixels to y-coord
  return

# do the same for player2!

# create the score board at the top of the screen
# set the text color, font, size, and position
pen = turtle.Turtle()
pen.speed(0)

# Keyboard binding
wn.listen() # listen for keyboard input
# bind the player<>_up and player<>_down functions to keys on the keyboard
# for example:
wn.onkey(player1_up,"w") # when user presses "w" on keyboard call function player1_up


# Main game loop
while True:
  wn.update()

  # clear the ball drawing
  # Move the ball by setting its x and y coordinates to be the current x and y coordinates plus the direction of movement in each direction
  # redraw the ball


  # Border checking
  # if the ball goes out of the screen's y value range, reverse the direction of movement in the y direction


  # if the ball goes out of the screen's x value range, that means that a player has gained points
  # reverse the direction of movement in the x direction
  # add a point to the corresponding player's score


  # Paddle and ball collisions
  # if the ball position comes near enough to the player position, reverse the ball's direction and send it toward the opposite player