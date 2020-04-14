import turtle, kotak
from random import random, choice

color = ["blue", "red", "yellow", "green", "cyan", "black"]
t = turtle.Turtle()
mybox = kotak.Square(x=10,y=10,width=10,color="black")
for i in range(10):
	px = int(random()*200)-100
	py = int(random()*200)-100
	w = int(random()*100)-50
	mybox.setProperties(x=px,y=py,width=w,color=choice(color))
	mybox.draw(t)

turtle.done()


