def draw_square(length):
    import math
    import turtle

# Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

# Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    for i in range(4):
      pen.forward(length)
      pen.right(90)

    pen.hideturtle()
    window.mainloop()


print(draw_square(100))