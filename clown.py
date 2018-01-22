import turtle #module tha drawn things

def draw_square():
    turtle.setworldcoordinates(-200, -400, 900, 900)
    background = turtle.Screen() #create the background
    background.bgcolor ("#005ce6") #background color
    
    tria = turtle.Turtle()
    tria.shape("arrow")
    tria.color("red","white")
    tria.speed(400)
    
    
    t = 1 #factor small triangle 4
    t2 =5 #big triangle quantity
    t3 = 5
    t1 = 5
    x = 300
    y = 300
    tria.penup()
    tria.setpos(x,y)
    tria.pendown()
    while t1 > 0:
        while t2 > 0:   #triangle unit
            while t3 > 0:
                while t > 0:
                    
                    tria.begin_fill()
                    tria.color("grey","yellow")
                    tria.left(120)
                    tria.forward(100)
                    tria.left(120)
                    #tria.forward(100)
                    tria.right(60)
                    tria.end_fill
                    t = t - 1
                t = 5
                tria.begin_fill
                tria.color("grey","blue")
                tria.left(120)
                tria.forward(100)
                tria.left(120)
                tria.forward(100)
                #tria.right(120)
                tria.end_fill
                t3 = t3 -1
            t3 = 5
            tria.begin_fill
            tria.color("grey","red")
            #tria.left(120)
            tria.forward(100)
            tria.left(120)
            tria.forward(100)
            tria.right(120)
            tria.end_fill
            t2 = t2 - 1
            
        t2 = 3
        tria.begin_fill
        tria.color("grey","green")
        tria.left(120)
        tria.forward(100)
        tria.left(120)
        tria.forward(100)
        tria.right(120)
        tria.end_fill
        t1 = t1 - 1
    t1 = 0
    background.exitonclick() #close background
draw_square()


