from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(500, 500)
screen.tracer(0)
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

# control snake
while game_on:

    def move_up():
        if snake_length[0].heading() == 270:
            pass
        else:
            if snake_length[0].heading() == 0:
                snake_length[0].left(90)
            elif snake_length[0].heading() == 180:
                snake_length[0].right(90)
            else:
                pass

    def move_down():
        if snake_length[0].heading() == 90:
            pass
        else:
            print(snake_length[0].heading())
            if snake_length[0].heading() == 0:
                snake_length[0].right(90)
            elif snake_length[0].heading() == 180:
                snake_length[0].left(90)
            else:
                pass

    def move_left():
        if snake_length[0].heading() == 0:
            pass
        else:
            print(snake_length[0].heading())
            if snake_length[0].heading() == 90:
                snake_length[0].left(90)
            elif snake_length[0].heading() == 270:
                snake_length[0].right(90)
            else:
                pass

    def move_right():
        if snake_length[0].heading() == 360:
            pass
        else:
            print(snake_length[0].heading())
            if snake_length[0].heading() == 90:
                snake_length[0].right(90)
            elif snake_length[0].heading() == 270:
                snake_length[0].left(90)
            else:
                pass

    screen.listen()
    screen.onkey(move_up, "w")
    screen.onkey(move_down, 's')
    screen.onkey(move_left, 'a')
    screen.onkey(move_right, 'd')

    screen.update()
    time.sleep(0.15)
    for r in range(len(snake_length)-1, 0, -1):
        snake_length[r].goto(snake_length[r-1].pos())
    snake_length[0].forward(20)

screen.exitonclick()
