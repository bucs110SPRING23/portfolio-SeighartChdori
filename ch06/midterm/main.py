import turtle

window = turtle.Screen()
turtle1 = turtle.Turtle()
turtle1.shape("turtle")


# Moves the turtle's X value without drawing anything
def moveTurtleX (turtle1, x) :
    turtle1.pu()
    turtle1.setx(x)
    turtle1.pd()

# Moves the turtle's Y value without drawing anything
def moveTurtleY (turtle1, y) :
    turtle1.pu()
    turtle1.sety(y)
    turtle1.pd()

#Moves both the X and Y value without drawing anything
def moveTurtleXY (turtle1, x, y):
    turtle1.pu()
    turtle1.setpos(x,y)
    turtle1.pd()

# Returns the current coordinates of the turtle
def returnPosition () :
    positionx = turtle1.xcor()
    positiony = turtle1.ycor()
    print ("The pens current coordinates are"+" ("+str(round(positionx)),str(round(positiony))+")")

turtle1.speed(6)

def main() :
# Drawing the toast
    moveTurtleXY(turtle1, -310, 300) #Crust

    turtle1.right(90)

    turtle1.color("black", "#b38545") #Fill Color
    turtle1.begin_fill()

    for i in range(4) :
        turtle1.pd()
        turtle1.fd(500)
        for y in range(4) :
            turtle1.left(22.5)
            turtle1.fd(25)

    turtle1.end_fill()
    returnPosition()

    turtle1.color("black","#d1be9d") #Fill Color
    turtle1.begin_fill()

    moveTurtleXY(turtle1, -260, 250) #Inner Toast

    for i in range(4) :
        turtle1.pd()
        turtle1.fd(400)
        for y in range(4) :
            turtle1.left(22.5)
            turtle1.fd(25)

    turtle1.end_fill()
    returnPosition()

    turtle1.pu()

    turtle1.color("black","#d5b872") #Fill Color

    '''
    Drawing the top of the toast (I think it looks better without the top of the toast.)
    for x in range(2) :
        turtle1.pd()
        turtle1.right(90*(x+1))
        turtle1.circle(125,180)
        turtle1.pu()
    '''

    turtle1.home()

    # Drawing the head
    moveTurtleY(turtle1,-150)
    turtle1.begin_fill()
    turtle1.circle(200)
    turtle1.end_fill()
    returnPosition()

    # Drawing the nose
    turtle1.color("black")
    moveTurtleXY(turtle1, 0, -50)
    turtle1.begin_fill()
    turtle1.circle(10)
    turtle1.end_fill()
    returnPosition()

    # Drawing the mouth
    turtle1.right(90)
    turtle1.circle(50,180)
    moveTurtleXY(turtle1, 0, -50)
    turtle1.right(180)
    turtle1.circle(-50,180)
    returnPosition()

    # Drawing the eyes
    moveTurtleXY(turtle1, -85, -10)
    turtle1.begin_fill()
    turtle1.circle(20)
    turtle1.end_fill()

    moveTurtleXY(turtle1, 85, -10)
    turtle1.begin_fill()
    turtle1.circle(-20)
    turtle1.end_fill()

    # Drawing the ears
    turtle1.color("black","#d5b872") #Fill Color
    moveTurtleXY(turtle1, 50, 245)
    turtle1.right(37)
    turtle1.begin_fill()
    turtle1.circle(-75,180)
    turtle1.end_fill()

    moveTurtleXY(turtle1, -50,245)
    turtle1.right(107)
    turtle1.begin_fill()
    turtle1.circle(75,180)
    turtle1.end_fill()

main() 
window.exitonclick()

