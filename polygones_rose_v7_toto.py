import turtle #module tha drawn things

def draw_square():
    turtle.setworldcoordinates(-300, -300, 600, 600)
    background = turtle.Screen() #create the background
    background.bgcolor ("#084B8A") #background color
    titi = turtle.Turtle()  #titi is an intance of Turtle class
    titi.shape("arrow")
    titi.color("#084B8A","black")
    titi.speed(200)
    toto = turtle.Turtle()  #titi is an intance of Turtle class
    toto.shape("arrow")
    toto.color("#084B8A","red")
    toto.speed(200)
    
    
    s = 10  #number of polygon sides
    n = s #counter
    x = 36 # counter of polygons
    d = 360/s #degrees in angle
    while x > 0:  #to draw in each degree of a circle
        while s > 0:
            titi.begin_fill()
            titi.left(d)
            titi.forward(105)
            titi.circle(25)
            toto.begin_fill()
            toto.left(d)
            toto.forward(100)
            toto.circle(25)
            s = s - 1
    
        x = x - 1
        s = n
        titi.right(10)
        titi.end_fill()
        toto.left(10)
        toto.end_fill()
    background.exitonclick() #close background
draw_square()


