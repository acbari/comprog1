import turtle

color = "red"
step= 100
x = 100
y = 100

t = turtle.Turtle()

t.penup()
t.goto(x, y)
t.width(1)
t.fillcolor(color)
t.begin_fill()
t.setheading(0)
t.pendown()
t.goto(x+step, y)
t.goto(x+step, y+step)
t.goto(x, y+step)
t.goto(x, y)
t.end_fill()
t.penup()

turtle.done()
