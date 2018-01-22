import turtle #module tha drawn things
def draw_square():
    turtle.setworldcoordinates(-300, -300, 600, 600)
    background = turtle.Screen() #create the background
    background.bgcolor ("#084B8A") #background color
    titi = turtle.Turtle()  #titi is an intance of Turtle class
    titi.shape("square")
    titi.color("white")
    titi.speed(100)
    puppy = turtle.Turtle() #another instance of Turtle class
    puppy.shape("circle")
    puppy.color("yellow")
    puppy.speed(100)
    reddy = turtle.Turtle() #another instance of Turtle class
    reddy.shape("circle")
    reddy.color("red")
    reddy.speed(200)
    s = 10 # number of sides
    x = s # counter ovewrall
    z = s # counter big
    w = s # counter small
    y = 360/s #angle
    while x > 0:
        while z > 0:
            titi_pos = titi.pos()
            reddy.setpos(titi_pos)
            titi.forward(100) #move the cursor and draw
            w = s
            puppy.setpos(titi_pos)
            while w > 0:
                puppy.forward(10)
                puppy.left(y)
                w = w - 1
                reddy.goto(titi_pos)
                reddy.circle(40)
                reddy.right(y)
            titi.left(y)  #rotate
            z = z - 1
            x = x - 1






    background.exitonclick() #cierra el background
draw_square()


