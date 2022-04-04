import turtle
import math

def setupWindow(myWindow=None):
  myWindow.setworldcoordinates(-360, -50, 360, 50)

def setupAxis(myTurtle=None, x_start = 0,y_start = 0, x_end = 0, y_end = 0):
  myTurtle.pu()
  myTurtle.goto(x_start,y_start)
  myTurtle.pd()
  myTurtle.goto(x_end,y_end)


def drawSineCurve(myTurtle=None):
  myTurtle.pu()
  myTurtle.goto(-360,0)
  myTurtle.pd()
  for angle in range(-360, 360):
    myTurtle.goto(angle, math.sin(math.radians(angle)))
  myTurtle.up()
  
def drawCosineCurve(myTurtle = None):
  myTurtle.color("blue")
  myTurtle.goto(-360,1)
  myTurtle.pd()
  for angle in range(-360, 360):
    myTurtle.goto(angle, math.cos(math.radians(angle)))

def drawTangentCurve(myTurtle = None):
  myTurtle.color("red")
  myTurtle.pu()
  myTurtle.goto(-360,0)
  myTurtle.pd()
  for angle in range(-360, 360):
    myTurtle.goto(angle, math.tan(math.radians(angle)))
  myTurtle.clear()

def harryPotter (turtle = None, length = None):
  dobby = turtle
  dobby.pensize(5)
  dobby.pu()
  dobby.goto(0,-25)
  dobby.pd()
  
  for i in range(3):
    dobby.forward(length)
    dobby.left(120)
    
  dobby.forward(length/2)
  dobby.circle(20)
  dobby.left(90)
  dobby.forward(55)

def fan ():
  question = input("Do you know the symbol of Deathly Hallows from Harry Potter?(yes/no): ")
  if question == "yes":
    harryPotter(turtle, 70 )
    print("YAY")
  else:
    print("boooo")
    return

def main():
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()

    setupWindow(wn)
    setupAxis(dart, 0, 2, 0, -2)
    setupAxis(dart, -360, 0, 360, 0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    fan()

    wn.exitonclick()
main()
