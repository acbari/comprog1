import xmltodict
import turtle

def xml2dict(xmlfile):
	#baca isi file xml kedalam string
	f = open(xmlfile,'r')
	xmlstr = f.read()
	f.close()
	#ubah xml menjadi tipe data dict
	flagdata = xmltodict.parse(xmlstr)
	#kembalikan semua command
	allcmd = flagdata["GraphicsCommands"]["Command"]
	return allcmd

t = turtle.Turtle()
cmdlist = xml2dict("flag.xml")

for cmd in cmdlist:
	t.penup()
	print(cmd)
	drawcmd = cmd["#text"]
	if drawcmd == "Rect":
		x = int(cmd["@x"])
		y = int(cmd["@y"])
		width = int(cmd["@width"])
		height = int(cmd["@height"])
		color = cmd["@color"]
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
	elif drawcmd == "Circle":
		x = int(cmd["@x"])
		y = int(cmd["@y"])
		radius = float(cmd["@radius"])
		color = cmd["@color"]
		t.fillcolor(color)
		t.begin_fill()
		t.width(1)
		t.goto(x,y)
		t.pendown()		
		t.circle(radius)
		t.end_fill()
		t.penup()
turtle.done()