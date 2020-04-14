import turtle, kotak
from random import random, choice

color = ["blue", "red", "yellow", "green", "cyan", "black"]
t = turtle.Turtle()
box = [] 
for i in range(10):
	px = int(random()*200)-100
	py = int(random()*200)-100
	w = int(random()*100)-50
	box.append(kotak.Square(x=px,y=py,width=w,color=choice(color)))
	box[i-1].draw(t)

turtle.done()


