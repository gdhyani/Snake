from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(500, 500)


snake = Turtle('square')
length = 3
snake.shapesize(1, length)
snake.penup()
snake.fillcolor('white')



screen.exitonclick()
