import turtle
num_sides = input("How many sides would you like your shape to have?\n")
length = input("How long would you like your sides to be?\n")
color = input("What color would you like your shape to be?\n")
window = turtle.Screen()
draw = turtle.Turtle()
draw.pd()
draw.color(color)
draw.circle(int(length),None,int(num_sides))

window.exitonclick()