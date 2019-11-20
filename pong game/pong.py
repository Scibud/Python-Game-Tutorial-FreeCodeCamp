import turtle
import winsound


# Game Window
wn = turtle.Screen()
wn.title("Pong as per @TokyoedTech Tutorial #FreeCodeCamp")
wn.bgcolor("black")
wn.setup(width=800, height=400)
wn.tracer(0)



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=3,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=3,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .1   # System speed plays a role, choose suitably
ball.dy = -.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,160)
pen.write("Player A: 0    Player B: 0",align="center",font=("Courier",14,"normal"))

score_a = 0
score_b = 0


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    if paddle_a.ycor() >  170:
        paddle_a.sety(170)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    if paddle_a.ycor() <  -170:
        paddle_a.sety(-170)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    if paddle_b.ycor() >  170:
        paddle_b.sety(170)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    if paddle_b.ycor() <  -170:
        paddle_b.sety(-170)



# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# Main GAme loop
while True:
    wn.update()


    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking the window
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1
        winsound.PlaySound("Various-13.wav",winsound.SND_ASYNC)

    if ball.ycor() < -190:
        ball.sety(-190)
        ball.dy *= -1
        winsound.PlaySound("Various-13.wav",winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    # Paddle & Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 30 and ball.ycor() > paddle_b.ycor() - 30):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Various-13.wav",winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 30 and ball.ycor() > paddle_a.ycor() - 30):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Various-13.wav",winsound.SND_ASYNC)