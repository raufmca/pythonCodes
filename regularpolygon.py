#Drawing polygon

import turtle
import random

# Draws a regular polygon with the given number of sides.
# The length of each side is length.
# The pen begins at point(x, y).
# The color of the polygon is color.

def polygon(sides, length, x, y, color):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    
    for i in range (sides):
        turtle.forward(length)
        turtle.left(360//sides)
    
    turtle.end_fill()
    
    turtle.hideturtle()
    turtle.tracer(0)
    

# Main program 

#polygon(4,5,2,10,"red")

for i in range(20):
    polygon(random.randrange(3, 11), random.randrange(5, 51), random.randrange(-150, 151),
            random.randrange(-150, 151), random.choice(("red", "green", "blue", "black", "yellow")))
    
turtle.update()
turtle.exitonclick()
    