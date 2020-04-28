import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(5)
tess.shape("circle")

def h1(x, y):
	tess.goto(x, y)
	
def h2(x, y):
	tess.penup()
	tess.goto(x, y)
	tess.pendown()

wn.onclick(h1,1)  
wn.onscreenclick(h2,3)  
wn.mainloop()


