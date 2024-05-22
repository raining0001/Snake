from turtle import Screen 
import time
from snake import Snake
from food import Food
from score import Score


screen = Screen() # create a screen
screen.setup(width=600, height=600) # set the screen size
screen.bgcolor("black") # set the background color
screen.title("Snake") # set the title
screen.tracer(0) # turn off the animation , otherwise the snake will move slowly

score = Score()

#create a snake
snake = Snake() # call Snake class and create a snake object
food = Food() 

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# create the snake movement
game_is_on = True   # set the game to be on
while game_is_on:   # while loop to keep the game running
    screen.update() # update the screen inside the while loop to avoid the snake lagging
    time.sleep(0.08) # set the speed of the snake

    snake.move()  
# detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

# detect colision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

# detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on = False
            score.game_over()
    # if head collides with any segment in the tail:
    # trigger game_over


screen.exitonclick()from turtle import Turtle 

POSITION = [(0, 0), (-20, 0), (-40, 0)] 
# set the snake segments initial position
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  
    def __init__(self):
      self.segments = [] 
# create an empty list to store the snake next positions
      self.create_snake()
      self.head = self.segments[0]
  
    def create_snake(self): # creates a method called create_snake , which creates the snake segments
      for position in POSITION: 
# a for loop to create the segments of the snake
        new_turtle = Turtle() 
# create a new turle
        new_turtle.shape("square") 
# give it the shape pf a square
        new_turtle.color("white") 
# set the color of the snake to white
        new_turtle.penup() 
# lifts the pen up so that it does not draw
        new_turtle.goto(position) 
# set the position of the turtle (here position is equal to the index in the list positions)
        self.segments.append(new_turtle) 
# add the new turtle element with the given position to the list segments

    def move(self):
      for seg_num in range(len(self.segments)-1, 0, -1):
          
# a for loop to move the snake segments from the last element to the n-1 element , in order to get the last position of the snake and move it to the position of the second to last element
          new_x = self.segments[seg_num-1].xcor() 
# get the x-coordinate of the element before the current element
          new_y = self.segments[seg_num-1].ycor()
# get the y-coordinate of the element before the current element
          self.segments[seg_num].goto(new_x, new_y) 
# move the current element to the position of the element before it
      self.head.forward(MOVE_DISTANCE)
      


    def up(self):
      if self.head.heading() != DOWN:
        self.head.setheading(UP)


    def down(self):
      if self.head.heading() != UP:
        self.head.setheading(DOWN)


    def left(self):
      if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)


    def right(self):
      if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)

    def add_segment(self,position): # creates a method called add_segment
      new_turtle = Turtle() 
      new_turtle.shape("square") 
      new_turtle.color("white") 
      new_turtle.penup() 
      new_turtle.goto(position) 
      self.segments.append(new_turtle)  

  
    def extend(self): # add a new segment to the snake
      self.add_segment(self.segments[-1].position()) # add a new segment to the snake at the position of the last segment


    def cretae_snake(self): # create the snake
      for position in POSITION: # a for loop to create the segments of the snake
        self.add_segment(position) # add a new segment to the snake at the position of the last segment

    
  
  
