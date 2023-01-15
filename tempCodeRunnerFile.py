    print(snake.heading())
        if snake.heading() == 90:
            snake.right(90)
        elif snake.heading() == 270:
            snake.left(90)
        else:
            pass
        snake.forward(100);
