import turtle #module tha drawn things

def draw_square():
    turtle.setworldcoordinates(-200, -400, 900, 900)
    background = turtle.Screen() #create the background
    background.bgcolor ("#005ce6") #background color
    
    tria = turtle.Turtle()
    tria.shape("arrow")
    tria.color("red","white")
    tria.speed(10)
    
    
    t = 10 #factor small triangle 4
    t2 = 2 #big triangle quantity
    t3 = t2
    x = 300
    y = 300
    tria.penup()
    tria.setpos(x,y)
    tria.pendown()
    while t2 > 0:   #triangle unit
        while t3 > 0:
            while t > 0:
                
                tria.begin_fill()

                tria.left(120)
                tria.forward(100)
                tria.left(120)
                tria.forward(100)
                tria.right(60)
                tria.end_fill
                tria.right(120)

                t = t - 1
                tria.right(30) #this angle modify all
            t = 3
           
            t3 = t3 -1
    
        t2 = t2 - 1
                
    
    
    
    


    



    background.exitonclick() #close background
draw_square()


