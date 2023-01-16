from turtle import Turtle, Screen
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(500, 500)
position = [(0, 0), (-20, 0), (-40, 0)]
snake_length = []
game_on = True
# snake on screen
for pos in position:
    snake = Turtle('square')
    snake.penup()
    snake.fillcolor('white')
    snake.setpos(pos)
    snake_length.append(snake)
screen.tracer(0)

# control snake
while game_on:
    for snake in snake_length:
        snake.forward(10)
        screen.update()
    time.sleep(1)


def move_up():
    if snake.heading() == 270:
        pass
    else:
        if snake.heading() == 0:
            snake.left(90)
        elif snake.heading() == 180:
            snake.right(90)
        else:
            pass


def move_down():
    if snake.heading() == 90:
        pass
    else:
        print(snake.heading())
        if snake.heading() == 0:
            snake.right(90)
        elif snake.heading() == 180:
            snake.left(90)
        else:
            pass


def move_left():
    if snake.heading() == 0:
        pass
    else:
        print(snake.heading())
        if snake.heading() == 90:
            snake.left(90)
        elif snake.heading() == 270:
            snake.right(90)
        else:
            pass


def move_right():
    if snake.heading() == 360:
        pass
    else:
        print(snake.heading())
        if snake.heading() == 90:
            snake.right(90)
        elif snake.heading() == 270:
            snake.left(90)
        else:
            pass


screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, 's')
screen.onkey(move_left, 'a')
screen.onkey(move_right, 'd')
screen.exitonclick()
