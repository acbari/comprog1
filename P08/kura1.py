import turtle

color = "red"
step= 100
x = 100
y = 100

t = turtle.Turtle()

turtle.penup()
turtle.goto(x, y)
turtle.width(1)
turtle.fillcolor(color)
#turtle.begin_fill()
turtle.setheading(0)
turtle.pendown()
turtle.goto(x+step, y)
turtle.goto(x+step, y+step)
turtle.goto(x, y+step)
turtle.goto(x, y)
#turtle.end_fill()
turtle.penup()

turtle.done()
