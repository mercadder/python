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
    puppy.color("orange")
    puppy.speed(100)
    reddy = turtle.Turtle() #another instance of Turtle class
    reddy.shape("circle")
    reddy.color("red")
    reddy.speed(200)
    s = 10 # number of sides
    x = s # counter overall
    z = s*2 # counter big
    w = s/2 # counter small
    y = 360/s #angle
    while x > 0:
        while z > 0:
            puppy_pos = puppy.pos()
            titi_pos = titi.pos()
            reddy_pos = reddy.pos()
            puppy.forward(100)
            puppy.left(y)
            
            titi.forward(s*20) #move the cursor and draw
            titi.circle(z*5)
            titi.left(y)
            w = s
            while w > 0:
                reddy.goto(puppy_pos)
                reddy.circle(w*10)
                reddy.left(y)
                reddy.forward(100)
                reddy.circle(s-2)
                titi.left(y)  #rotate
                w = w - 1
            
            z = z - 1
        x = x - 1
        
    background.exitonclick() #cierra el background
draw_square()


