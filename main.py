import turtle
import math

def setupWindow(myWindow=None):
  myWindow.setworldcoordinates(-360, -1, 360, 1)
  
def setupAxis(myTurtle=None):
  myTurtle.down()
  myTurtle.goto(-360,0)
  myTurtle.goto(360,0)
  myTurtle.up()
  myTurtle.goto(0,2)
  myTurtle.down()
  myTurtle.goto(0,-2)
  myTurtle.up()

def drawSineCurve(myTurtle=None):
  myTurtle.color("orange")
  myTurtle.up()
  myTurtle.goto(-360,0)
  myTurtle.down()
  for angle in range(-360, 360):
    myTurtle.goto(angle, math.sin(math.radians(angle)))
  
def drawCosineCurve(myTurtle=None):
  myTurtle.color("blue")
  myTurtle.up()
  myTurtle.goto(-360,1)
  myTurtle.down()
  for angle in range(-360, 360):
    myTurtle.goto(angle, math.cos(math.radians(angle)))

def drawTangentCurve(myTurtle=None):
  myTurtle.color("red")
  myTurtle.up()
  myTurtle.goto(-360,0)
  myTurtle.down()
  for angle in range(-360, 360):
    myTurtle.goto(angle, math.tan(math.radians(angle)))


##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
