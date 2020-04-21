import XMLreader, turtle, sys
commandList, xList, yList, widthList, heightList, \
	colorList, radiusList = XMLreader.readXML(sys.argv[1])
t = turtle.Turtle()
screen = t.getscreen()
screen.colormode(255)
screen.tracer(0)
for i in range(len(commandList)):
	command = commandList[i]
	if command == "PenUp":
		t.penup()
	elif command == "PenDown":
		t.pendown()
	elif command == "GoTo":
		x = float(xList[i])
		y = float(yList[i])
		width = float(widthList[i])
		color = colorList[i]
		t.width(width)
		t.color(color)
		t.goto(x,y)
	elif command == "Circle":
		radius = float(radiusList[i])
		width = float(widthList[i])
		color = colorList[i]
		t.width(width)
		t.pencolor(color)
		t.circle(radius)
	elif command == "BeginFill":
		color = colorList[i]
		t.fillcolor(color)
		t.begin_fill()
	elif command == "EndFill":
		t.end_fill()
	else:
		print("Unknown Command:",command)
screen.update()
screen.exitonclick()

