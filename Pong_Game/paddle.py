from turtle import Turtle

# STARTING_POSITION = [350, 20]


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # def new_self(self):
    #     for position in STARTING_POSITION:
    #         self.new_self(position)
    #
    #
    # def new_self():
    #     self = Turtle('sqare')
    #     self.shapesize(stretch_wid=20, stretch_len=100)
    #     self.goto(350, 20)
    #     self.color('white')
    #     self.penup()
