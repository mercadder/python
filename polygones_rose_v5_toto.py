import turtle #module tha drawn things
def draw_square():
    turtle.setworldcoordinates(-300, -300, 600, 600)
    background = turtle.Screen() #create the background
    background.bgcolor ("#084B8A") #background color
    titi = turtle.Turtle()  #titi is an intance of Turtle class
    titi.shape("arrow")
    titi.color("yellow")
    titi.speed(100)
    toto = turtle.Turtle()  #titi is an intance of Turtle class
    toto.shape("arrow")
    toto.color("red")
    toto.speed(200)
    
    
    s = 4  #number of polygon sides
    n = s #counter
    x = 100 # counter of polygons
    d = 360/s #degrees in angle
    while x > 0:  #to draw in each degree of a circle
        while s > 0:
            titi.left(d)
            titi.forward(100)
            toto.left(d)
            toto.forward(50)
            s = s - 1
        x = x - 1
        s = n
        titi.right(20)
        toto.left(10)

    background.exitonclick() #close background
draw_square()


