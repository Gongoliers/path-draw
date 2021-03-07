import turtle

scale = 20
offset_x = scale * 15
offset_y = scale * 7.5


def draw_rectangle(width, height, color):
    global scale
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(width * scale)
    turtle.right(90)
    turtle.forward(height * scale)
    turtle.right(90)
    turtle.forward(width * scale)
    turtle.right(90)
    turtle.forward(height * scale)
    turtle.end_fill()


def move(x, y):
    global scale
    turtle.penup()
    turtle.goto((x * scale - offset_x, y * scale - offset_y))
    turtle.pendown()


def draw_path(x, y, path):
    global scale
    turtle.setheading(0)
    move(x, y)
    turtle.speed(speed=1)
    for p in path.path:
        if p[1]:
            # Rotation
            turtle.right(p[0])
        else:
            turtle.forward(p[0] * scale)
