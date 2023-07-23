#I learned to make the Pong game here: https://www.freecodecamp.org/news/how-to-code-pong-in-python/
#Debugging help provided by the amazing 24/7 chatGPT

import turtle

#game screen size
turtle.setup(800, 600)

#game screen background color
turtle.bgcolor("black")

#Left side paddle (Player 1)
Paddle1 = turtle.Turtle()
Paddle1.shape("square")
Paddle1.color("purple")
#Stretching the square to be a normal pong rectangle
Paddle1.shapesize(stretch_wid=5, stretch_len=1)
Paddle1.penup()
Paddle1.goto(-350, 0)
Paddle1.dy = 0

#Right side paddle (Player 2)
Paddle2 = turtle.Turtle()
Paddle2.shape("square")
Paddle2.color("green")
#Stretching the square to be a normal pong rectangle
Paddle2.shapesize(stretch_wid=5, stretch_len=1)
Paddle2.penup()
Paddle2.goto(350, 0)
Paddle2.dy = 0

#The ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = 0

#setting up the game rules
Game_Over = False
Winner = None
Points = {
    "Player1": 0,
    "Player2": 0
}

Game_Rules = {
    "MaxPoints": 3,
    "BallSpeed": 10
}

# The ball initial speed
ball.dx = Game_Rules["BallSpeed"]
ball.dy = -Game_Rules["BallSpeed"]

#Displaying the score
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0 Player 2: 0", align="center", font=("Arial", 24, "normal"))

# Function to update paddle and ball positions
def update_positions():
    global Game_Over, Winner

    # Move paddles
    Paddle1.sety(Paddle1.ycor() + Paddle1.dy)
    Paddle2.sety(Paddle2.ycor() + Paddle2.dy)

    # Check for paddle collision with the screen boundaries
    for paddle in [Paddle1, Paddle2]:
        if paddle.ycor() > 250:
            paddle.sety(250)
        elif paddle.ycor() < -250:
            paddle.sety(-250)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for ball collision with the top and bottom screen boundaries
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.sety(290 if ball.ycor() > 0 else -290)
        ball.dy *= -1

    # Check for ball collision with the paddles
    if (ball.xcor() > 330 and ball.xcor() < 340) and (Paddle2.ycor() + 50 > ball.ycor() > Paddle2.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
    elif (ball.xcor() < -330 and ball.xcor() > -340) and (Paddle1.ycor() + 50 > ball.ycor() > Paddle1.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1

    # Check for scoring points
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        Points["Player1"] += 1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        Points["Player2"] += 1

    # Update the score text
    score_display.clear()
    score_display.write("Player 1: {}   Player 2: {}".format(Points["Player1"], Points["Player2"]), align="center", font=("Arial", 24, "normal"))

    # Check for game over
    if Points["Player1"] == Game_Rules["MaxPoints"] or Points["Player2"] == Game_Rules["MaxPoints"]:
        Game_Over = True
        Winner = "Player1" if Points["Player1"] > Points["Player2"] else "Player2"

    if not Game_Over:
        turtle.ontimer(update_positions, 50)  # Repeat the update after 50 milliseconds

# Adding the user input controls

# Move paddle 1 up
def Paddle1Up():
    Paddle1.dy = 10

# Move paddle1 down
def Paddle1Down():
    Paddle1.dy = -10

# Move paddle2 up
def Paddle2Up():
    Paddle2.dy = 10

# Move paddle2 down
def Paddle2Down():
    Paddle2.dy = -10

# Binding the keys
turtle.listen()
turtle.onkeypress(Paddle1Up, "w")
turtle.onkeypress(Paddle1Down, "s")
turtle.onkeypress(Paddle2Up, "Up")
turtle.onkeypress(Paddle2Down, "Down")

# Creating the Game Over screen
if Game_Over:
    Game_Over_display = turtle.Turtle()
    Game_Over_display.color("white")
    Game_Over_display.penup()
    Game_Over_display.hideturtle()
    Game_Over_display.goto(0, 0)
    Game_Over_display.write("Game Over! {} wins!".format(Winner), align="center", font=("Arial", 36, "normal"))

#Start game loop
while not Game_Over:
    update_positions()
    turtle.update()
