import turtle

class Square:
    def __init__(self, x=0, y=0, width=100):
        self.x = x
        self.y = y
        self.width = width
        self.color = "red"
        self.outline = "black"
        self.edgeWidth = 1
	
    def getHeading(self):
        return self.t.heading

    def draw(self, turtle):
        turtle.penup ()
        turtle.goto(self.x, self.y)
        turtle.width(self.edgeWidth )
        if self.color != "transparent":
            turtle.fillcolor(self.color)
        else:
            self.color=self.outline
        turtle.fillcolor(self.color)
        if self.color != "transparent":
            turtle.begin_fill()
        turtle.pendown()
        turtle.setheading(0)
        turtle.goto(self.x+self.width,self.y)
        turtle.goto(self.x+self.width,self.y+self.width)
        turtle.goto(self.x,self.y+self.width)
        turtle.goto(self.x,self.y)
        if self.color != "transparent":
            turtle.end_fill()
        turtle.penup()

kotak = Square()
t = turtle.Turtle()
kotak.draw(t)
turtle.done()