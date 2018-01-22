import turtle #module tha drawn things

def draw_square():
    turtle.setworldcoordinates(-200, -400, 900, 900)
    background = turtle.Screen() #create the background
    background.bgcolor ("#005ce6") #background color
    titi = turtle.Turtle()  #titi is an intance of Turtle class
    titi.shape("arrow")
    titi.color("grey","#cc0066")
    titi.speed(200)
    toto = turtle.Turtle()  #toto is an intance of Turtle class
    toto.shape("arrow")
    toto.color("grey","white")
    toto.speed(200)
    titi.setpos(0,300)
    toto.penup()
    toto.setpos(200,700)
    toto.pendown()
    tria = turtle.Turtle()
    tria.shape("arrow")
    tria.color("red","white")
    tria.speed(10)
    tria.penup()
    tria.setpos(300,-200)
    tria.pendown()
    
    
    
    s = 4  #number of polygon sides
    t = 4 #factor small triangle
    t2 = 3 #big triangle quantity
    t3 = t2
    factor_ang = 3
    step = 100
    n = s #counter
    x = 8 # counter of polygons
    d = 360/s #degrees in angle
    ang_obtuso = 360/factor_ang
    ang_agudo = (360-ang_obtuso*2)/2
    
    while x > 0:  #to draw in each degree of a circle
        while s > 0:
            titi.begin_fill()#rose
            titi.left(ang_obtuso)
            titi.forward(150)
            titi.left(ang_agudo)
            titi.forward(50)
            
            toto.begin_fill()#cloud
            toto.circle(30)
            toto.forward(30)
            toto.left(20)
            toto.back(20)
            toto.circle(30)
            while t2 > 0:   #triangle unit
                while t3 > 0:
                    while t > 0:   #small triangles
                        
                        tria.begin_fill()
                        tria.forward(200)
                        tria.left(120)
                        tria.forward(200)
                        tria.left(120)
                        tria.forward(100)
                        tria.left(120)
                        tria.forward(100)
                        tria.left(120)
                        tria.forward(100)
                        tria.left(120)
                        tria.forward(100)
                        tria.left(120)
                        tria.forward(100)
                        tria.left(120)
                        tria.end_fill
                        t = t - 1
                    
                
                
                
                
                
                    t3 = t3 -1
                t2 = t2 - 1
                
            s = s - 1
    
        x = x - 1
        s = n
        titi.right(ang_agudo)
        titi.right(ang_obtuso)
        titi.end_fill()
        toto.right(20)
        titi.right(45)
        toto.end_fill()
    titi.color("black","#005ce6")
    titi.right(90)
    titi.forward(500)
    titi.right(90)
    titi.forward(100)
    titi.back(200)
    
    toto.penup()#sun
    toto.setpos(600,780)
    toto.pendown()
    toto.color("grey","yellow")
    toto.begin_fill()
    toto.circle(30)
    toto.end_fill()

    tria.setpos(600,-200)
    tria.penup()
    
    tria.right(120)
    tria.pendown()

    t = 3
    t3 = 3
    while t3 > 0:
        while t > 0:   #small triangles

            tria.begin_fill()
            tria.forward(200)

            tria.left(120)
            tria.forward(200)
            tria.left(120)
            tria.forward(100)
            tria.left(120)
            tria.forward(100)
            tria.left(120)
            tria.forward(100)
            tria.left(120)
            tria.forward(100)
            tria.left(120)
            tria.forward(100)
            tria.left(120)
            t = t - 1
        t3 = t3 -1
    








    background.exitonclick() #close background
draw_square()


