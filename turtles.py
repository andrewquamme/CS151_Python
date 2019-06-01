import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(75)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(50)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)

    for i in range(1,37):
        draw_square(brad)
        draw_triangle(brad)
        brad.right(10)

    brad.right(90)
    brad.forward(250)
    
    window.exitonclick()

draw_art()
