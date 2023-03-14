import turtle 
window = turtle.Screen()
draw = turtle.Turtle()
draw.shape("turtle")

#First Square
draw.color("purple")
draw.pd()
draw.circle(50,None,4)

#Second Square
draw.pu()
draw.goto(90,90)
draw.color("red")
draw.pd()
draw.circle(50,None,4)


window.exitonclick()
