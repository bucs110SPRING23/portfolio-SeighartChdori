import turtle
import random

window = turtle.Screen()
window.screensize(480,480)
size = window.screensize()
turtle = turtle.Turtle()
turtle.speed(0)

while (abs(turtle.xcor()) < size[0]) and (abs(turtle.ycor()) < size[1]) :
    
     flip = random.randint(1,2)
     if flip == 1 :
         turtle.left(90)
     elif flip == 2 :
        turtle.right(90)

     turtle.fd(50)

turtle.clear()
