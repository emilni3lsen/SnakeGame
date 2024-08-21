from turtle import Turtle
import random


FOOD_SIZE = 0.4


class Food(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(FOOD_SIZE, FOOD_SIZE)
        self.color("red")
        self.speed(0)
        self.refresh()
        
        
    def refresh(self):
        self.setpos(random.randint(-280, 280), random.randint(-280, 280))