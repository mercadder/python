import turtle #module tha drawn things
def draw_square():
    background = turtle.Screen() #create the background
    background.bgcolor ("red")
    titi = turtle.Turtle()  #
    x = 8 # number of sides and counter
    z = x # numer of polygone sides
    y = 360/z #angle
    while x > 0:
     titi.forward(100) #move the cursor and draw
     titi.left(y)  #rotate
     x = x - 1
    
    background.exitonclick() #cierra el background

draw_square()
