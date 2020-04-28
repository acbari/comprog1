import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)

def h1():
	tess.forward(30)
	tess.right(45)
	wn.ontimer(h1, 2000)

wn.ontimer(h1, 2000)
wn.mainloop()



