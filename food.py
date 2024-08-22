from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = ((randint(0, 28)) * 20) - 260
        random_y = ((randint(0, 28)) * 20) - 260
        self.goto(random_x, random_y)