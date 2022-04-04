import turtle
import math

def setupWindow(myWindow=None):
  '''
  sets size for window that the turtle can use
  args: (Window) - sets coordinate for window 
  retrun none 
  '''
  myWindow.setworldcoordinates(-360, -2, 360, 2)

def setupAxis(myTurtle=None):
  '''
  draws x and y axis
  args: (Turtle Object) - the turtle draws the axis
  return none
  '''
  myTurtle.down()
  myTurtle.goto(-360,0)
  myTurtle.goto(360,0)
  myTurtle.up()
  myTurtle.goto(0,2)
  myTurtle.down()
  myTurtle.goto(0,-2)
  myTurtle.up()


def drawSineCurve(myTurtle=None, myColor = ""):
  '''
  draw sine curve from -2pi to 2pi
  args: (Turtle Object) - the turtle draws sine, (myColor) - color of turtle pen
  Return none
  '''
  myTurtle.pu()
  myTurtle.color(myColor)
  myTurtle.goto(-360,0)
  myTurtle.pd()
  for angle in range(-360, 360):
    myTurtle.goto(angle, math.sin(math.radians(angle)))
  myTurtle.up()
  
def drawCosineCurve(myTurtle = None, myColor = ""):
  '''
  draw cosine curve from -2pi to 2pi
  args: (Turtle Object) - the turtle draws sine, (myColor) - color of turtle pen 
  Return none
  '''
  myTurtle.color(myColor)
  myTurtle.goto(-360,1)
  myTurtle.pd()
  for angle in range(-360, 360):
    myTurtle.goto(angle, math.cos(math.radians(angle)))

def drawTangentCurve(myTurtle = None, myColor = ""):
  '''
  draw tan curve from -2pi to 2pi
  args: (Turtle Object) - the turtle draws sine, (myColor) - color of turtle pen  
  Return none
  '''
  myTurtle.color(myColor)
  myTurtle.pu()
  myTurtle.goto(-360,0)
  myTurtle.pd()
  for angle in range(-360, 360):
    myTurtle.goto(angle, math.tan(math.radians(angle)))
  myTurtle.clear()

def harryPotter (turtle = None):
  '''
  draw deathly hallow logo from Harry Potter 
  args: (Turtle Object) - the turtle draws logo,
  Return none 
  '''
  dobby = turtle
  dobby.goto(0,-2)
  dobby.pd()
  dobby.goto(-180,-2)
  dobby.goto(0,2)
  dobby.goto(180,-2)
  dobby.goto(0,-2)
  dobby.circle(2)
  dobby.goto(0,2)
  
def fan():
  '''
  draw sine curve from -2pi to 2pi
  args: (Turtle Object) - the turtle draws sine,
  what type of oject, why pass it 
  '''
  question = input("Do you know the symbol of Deathly Hallows from Harry Potter?(yes/no): ")
  if question == "yes":
    harryPotter(turtle)
    print("YAY! ")
  else:
      print("boooo")
      return

def cube (num_input):
  num_input = int(input("Please input a number: "))
  return num_input * num_input * num_input
  

def main():
  wn = turtle.Screen()
  wn.tracer(5)
  dart = turtle.Turtle()

  setupWindow(wn)
  setupAxis(dart, 0, 2, 0, -2)
  setupAxis(dart, -360, 0, 360, 0)
  drawSineCurve(dart, "purple")
  drawCosineCurve(dart, "blue")
  drawTangentCurve(dart, "red")
  fan()

  result = cube()
  print(result)
  
  wn.exitonclick()
main()
