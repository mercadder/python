import turtle #module tha drawn things

def draw_square():
    turtle.setworldcoordinates(-300, -300, 600, 600)
    background = turtle.Screen() #create the background
    background.bgcolor ("#084B8A") #background color
    titi = turtle.Turtle()  #titi is an intance of Turtle class
    titi.shape("arrow")
    titi.color("#084B8A","red")
    titi.speed(500)
    toto = turtle.Turtle()  #titi is an intance of Turtle class
    toto.shape("arrow")
    toto.color("red")
    toto.speed(100)
    
    
    s = 5  #number of polygon sides
    n = s #counter
    x = 50 # counter of polygons
    d = 360/s #degrees in angle
    while x > 0:  #to draw in each degree of a circle
        while s > 0:
            titi
            titi.begin_fill()
            titi.left(d)
            titi.forward(150)
            titi.circle(x)
            toto.left(d)
            toto.forward(200)
            
            s = s - 1
        titi.end_fill()
        x = x - 1
        s = n
        titi.right(10)
        toto.left(20)

    background.exitonclick() #close background
draw_square()


