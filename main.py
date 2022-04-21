from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("bitter")
screen.tracer(0)

paddle = Paddle((0, -280))
ball = Ball()

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

positions = [(-380, 280), (-300, 280), (-210, 280), (-160, 280), (0, 280), (100, 280)]
bricks = []
for pos in positions:
    bricks.append(Brick(pos))

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()

    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.destroy()

    if ball.ycor() < -280:
        ball.reset_position()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.distance(paddle) < 30 and ball.ycor() < -250:
        ball.bounce_y()

screen.exitonclick()
