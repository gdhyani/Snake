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