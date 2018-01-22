import turtle #module that draw things

def draw_square():
    turtle.setworldcoordinates(-200, -400, 900, 900)
    background = turtle.Screen() #create the background
    background.bgcolor ("#005ce6") #background color
    
    tria = turtle.Turtle()
    tria.shape("arrow")
    tria.color("red","white")
    tria.speed(400)
    
    
    t = 2 #factor small triangle 4
    t2 =1 #big triangle quantity
    t3 = 2
    t1 = 7
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
                    tria.forward(50)
                    tria.right(120)
                    tria.end_fill
                    t = t - 1
                t = 3
                tria.begin_fill
                tria.color("grey","blue")
                tria.left(120)
                tria.forward(150)
                tria.left(120)
                tria.forward(150)
                
                tria.end_fill
                t3 = t3 -1
            t3 = 2
            tria.begin_fill
            tria.color("grey","red")
            #tria.left(120)
            tria.forward(100)
            tria.left(120)
            tria.forward(100)
        
            tria.right(120)
            tria.end_fill
            t2 = t2 - 1
            
        t2 = 2
        tria.begin_fill
        tria.color("grey","green")
        tria.right(120)
        tria.forward(100)
        tria.left(120)
        tria.forward(100)
        #tria.right(120)
        tria.back(100)
        tria.right(120)
        tria.end_fill
        t1 = t1 - 1
    t1 = 0
    background.exitonclick() #close background
draw_square()


