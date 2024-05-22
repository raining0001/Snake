from turtle import Turtle

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

  def create_snake(
      self
  ):  # creats a methode called create_snake , wich creates the snake segments
    for position in POSITION:
      # a for loop to create the sefments of the snake
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
    for seg_num in range(len(self.segments) - 1, 0, -1):

      # a for loop to move the snake segments from the last element to the n-1 element , in order to get the last position of the snake and move it to the position of the second to last element
      new_x = self.segments[seg_num - 1].xcor()
      # get the x-coordinate of the element before the current element
      new_y = self.segments[seg_num - 1].ycor()
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

  def add_segment(self, position):  # creats a methode called add_segment
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(position)
    self.segments.append(new_turtle)

  def extend(self):  # add a new segment to the snake
    self.add_segment(self.segments[-1].position(
    ))  # add a new segment to the snake at the position of the last segment

  def cretae_snake(self):  # create the snake
    for position in POSITION:  # a for loop to create the segments of the snake
      self.add_segment(
          position
      )  # add a new segment to the snake at the position of the last segment
