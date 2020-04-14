class Square:
	def __init__(self, **kwargs):
		self.x = kwargs["x"]
		self.y = kwargs["y"]
		self.width = kwargs["width"]
		self.color = kwargs["color"]
		self.edgeWidth = 1

	def setProperties(self, **kwargs):
		self.x = kwargs["x"]
		self.y = kwargs["y"]
		self.width = kwargs["width"]
		self.color = kwargs["color"]
		self.edgeWidth = 1

	def draw(self, turtle):
		turtle.penup ()
		turtle.goto(self.x, self.y)
		turtle.width(self.edgeWidth )
		turtle.fillcolor(self.color)
		turtle.begin_fill()
		turtle.setheading(0)
		turtle.pendown()
		turtle.goto(self.x+self.width,self.y)
		turtle.goto(self.x+self.width,self.y+self.width)
		turtle.goto(self.x,self.y+self.width)
		turtle.goto(self.x,self.y)
		turtle.end_fill()
		turtle.penup()

if __name__ == "__main__":
	import turtle
	t = turtle.Turtle()
	kotak = Square(x=10, y=10, width= 100, color="blue")
	kotak.draw(t)
	kotak.setProperties(x=-20, y=-20, width= -50, color="red")
	kotak.draw(t)
	
	turtle.done()