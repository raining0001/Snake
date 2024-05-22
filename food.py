from turtle import Turtle
import random

class Food(Turtle): # creates a class called Food , which inherits from the Turtle class
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len=0.5,stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
    self.refresh()


  def refresh(self): # creates a method called refresh
    random_x = random.randint(-280,280) # creates a random x-coordinate between -280 and 280
    random_y = random.randint(-280,280) # create a random y-coordinate between -280 and 280
    self.goto(random_x,random_y) # moves the turtle  object to the random position
    

    
