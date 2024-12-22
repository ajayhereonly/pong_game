from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen= Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard= Scoreboard()



paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)

paddle.penup()

paddle.goto(350,0)




screen.listen()
screen.onkey(r_paddle.go_up,"o")
screen.onkey(r_paddle.go_down,"l")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() >280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()



    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("made contact")
        ball.bounce_x()


    #detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect L padal misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()

