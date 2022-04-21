from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=3, stretch_len=2)
        self.penup()
        self.goto(position)

    def destroy(self):
        self.hideturtle()
