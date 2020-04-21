import turtle, xmltodict, sys
from random import choice

screen = turtle.Screen()
allRect = []
allCircle = []
allTriangle = []
mode = 0
isdrawing = False
t = turtle.Turtle()
t.penup()
colorlist = ["blue", "red", "yellow", "green", "cyan", "black", "orange"]

fname = sys.argv[1]

def addRect(x,y,width,height,color):
	rect = {}
	rect["x"] = x
	rect["y"] = y
	rect["width"] = width
	rect["height"] = height
	rect["color"] = color
	return rect

def addCircle(x,y,radius,color):
	rect = {}
	rect["x"] = x
	rect["y"] = y
	rect["radius"] = radius
	rect["color"] = color
	return rect

def addTriangle(x,y,width,color):
	rect = {}
	rect["x"] = x
	rect["y"] = y
	rect["width"] = width
	rect["color"] = color
	return rect

def drawRect(x,y,width,height,color):
	global isdrawing
	isdrawing = True
	t.fillcolor(color)
	t.begin_fill()
	t.width(1)
	t.goto(x,y)
	t.pendown()
	t.goto(x+width,y)
	t.goto(x+width,y+height)
	t.goto(x,y+height)
	t.goto(x,y)
	t.end_fill()
	t.penup()
	isdrawing = False

def drawCircle(x,y,radius,color):
	global isdrawing
	isdrawing = True
	t.fillcolor(color)
	t.begin_fill()
	t.width(1)
	t.goto(x,y)
	t.pendown()		
	t.circle(radius)
	t.end_fill()
	t.penup()
	isdrawing = False

def drawTriangle(x,y,width,color):
	global isdrawing
	isdrawing = True
	t.fillcolor(color)
	t.begin_fill()
	t.width(1)
	t.goto(x,y)
	t.pendown()		
	t.goto(x+width,y)
	t.goto(x+width,y+width)
	t.goto(x,y)
	t.end_fill()
	t.penup()
	isdrawing = False

def newRect():
	print("mode rectangle")
	global mode
	mode = 0

def newCircle():
	print("mode circle")
	global mode
	mode = 1
	
def newTriangle():
	print("mode triangle")
	global mode
	mode = 2
	
def placeIt(x,y):
	if not(isdrawing):
		print(x,y)
		print(mode)	
		if mode == 0:
			drawRect(x,y,50,50,choice(colorlist))
			allRect.append(addRect(x,y,50,50,choice(colorlist)))
		elif mode == 1:
			drawCircle(x,y-20,20,choice(colorlist))
			allCircle.append( addCircle(x,y-20,20,choice(colorlist)) )
		elif mode == 2:
			drawTriangle(x,y,50,choice(colorlist))
			allTriangle.append( addTriangle(x,y,50,choice(colorlist)) )

screen.onkey(newRect, "r")
screen.onkey(newCircle, "c")
screen.onkey(newTriangle, "t")
screen.onclick(placeIt)

screen.listen()
turtle.done()

geometry = {}
geometry["rect"] = allRect
geometry["circle"] = allCircle
geometry["triangle"] = allTriangle
allitems = {}
allitems["root"] = geometry
xml_str = xmltodict.unparse(allitems, pretty=True)

f = open(fname+".xml",'w')
f.write(xml_str)
f.close()