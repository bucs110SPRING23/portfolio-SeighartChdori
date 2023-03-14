import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.speed(1)
leonardo.speed(1)

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

# Race 1
michelangelo.fd(random.randrange(1,101))
leonardo.fd(random.randrange(1,101))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Race 2
for _ in range(10) :
    michelangelo.fd(random.randrange(1,11))
    leonardo.fd(random.randrange(1,11))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

window.exitonclick()

# PART B - complete part B here
import math
import pygame

pygame.init()
window = pygame.display.set_mode()

num_sides = [3,4,6,20,100,360]
points = []
side_length = 500
xpos = 990
ypos = 540

for x in range(len(num_sides)) :

    for y in range(num_sides[x]) :
        angle = math.radians((360/num_sides[x]) * y)
        xpos1 = xpos + side_length * math.cos(angle)
        ypos1 = ypos + side_length * math.sin(angle) 
        points.append([xpos1,ypos1])
   
    window.fill("black")
    pygame.display.flip()
    pygame.draw.polygon( window , "red" , points )
    pygame.display.flip()
    pygame.time.wait(2000)
    
    points.clear()
    