from turtle import Turtle

FONT = ("Arial",20,"normal") # creates a constant for the font , size and style

class Score(Turtle): # creates a class called Score , which inherits from the Turtle class
  def __init__(self): # creates a constructor
    super().__init__() # calls the constructor of the parent class
    self.score = 0 # creates a variable called score and sets it to 0
    self.hideturtle() # hides the turtle
    self.penup() # lifts the pen up
    self.goto(0,260) # moves the turtle to the top of the screen
    self.color("white") 
    self.update_score() # calls the update_score method


  def update_score(self): # creates a method called update_score
    self.write(f"Score: {self.score}",align="center",font=FONT) # writes the score on the screen
    
  def increase_score(self): # creates a method called increase_score
    self.score +=1 # increases the score by 1
    self.clear() # clears the previous score
    self.update_score() # calls the update_score method
    
  def game_over(self): # creates a method called game_over
    self.penup() 
    self.hideturtle()
    self.goto(0,0)    
    self.write("GAME OVER",align="center",font = FONT)
    self.color("white")
    