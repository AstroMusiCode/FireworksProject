import turtle

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("black")
myTurtle.speed(100)
# Firework 1
myTurtle.penup()
myTurtle.setposition(-100,100)
myTurtle.pendown()
for i in range(int(360 / 6)):
    myTurtle.color("red")
    myTurtle.forward(50)
    myTurtle.backward(50)
    myTurtle.right(6)

# Firework 2
def initReset(x,y):
    myTurtle.penup()
    myTurtle.setposition(x, y)
    myTurtle.pendown()
    myTurtle.color("blue")
def makeUpperSegment(l, v):
    myTurtle.left(45)
    if (v == 1):
        myTurtle.forward(int(l / 2))
    else:
        myTurtle.forward(l)
    myTurtle.right(90)
    if (v == 1):
        myTurtle.forward(l)
    else:
        myTurtle.forward(int(l / 2))   
def makeLowerSegment(l, v):
    if (v == 1):
        myTurtle.forward(int(l / 2))
    if (v == 1):
        myTurtle.left(90)
    else:
        myTurtle.right(45)
    myTurtle.forward(l)
    if (v == 1):
        myTurtle.right(45)
    else:
        myTurtle.left(90)
    if (v == 2):
        myTurtle.forward(int(l/2))
def makeLine(x, y, turn, moveVal):
    myTurtle.penup()
    myTurtle.setposition(x, y)
    myTurtle.right(turn)
    myTurtle.pendown()
    myTurtle.forward(moveVal)

initReset(100, 100)
makeUpperSegment(50, 1)
myTurtle.left(45)
makeUpperSegment(50, 2)

initReset(100,75)
makeLowerSegment(50, 1)
makeLowerSegment(50, 2)

makeLine(152.5, 125, 45 + 90, 75)
makeLine(100, 87.5, -90, 100)

# Firework 3
def initReset2(x, y):
    myTurtle.penup()
    myTurtle.setposition(x, y)
    myTurtle.color("green")
    myTurtle.pendown()
def makeCircleFirework(circleSize, circleAmount):
    for i in range(int(360 / circleAmount)):
        myTurtle.circle(circleSize)
        myTurtle.right(circleAmount)
        myTurtle.forward(circleSize)

initReset2(0,0)
makeCircleFirework(5, 5)

input()