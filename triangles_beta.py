import turtle #module that draw things
import math

def draw_plotter():
    turtle.setworldcoordinates(-200, -200, 1000, 1000)
    background = turtle.Screen() #create the background
    background.bgcolor ("#005ce6") #background color
    
    plot = turtle.Turtle()
    plot.shape("arrow")
    plot.color("red","white")
    plot.speed(1)
    x = 0
    y = 0
    q = 4
    m = 2
   
    
    T = 3 #number of internal triangles, counter
    L = 300 #length of side
    h = math.sqrt((L/4.0)**2-(L/16.0)**2) #height small triangle
    S = T # shape counter
    plot.up()
    plot.setpos(x,y)
    plot.down()
    
    plot.setpos(x+L/m,y)
    while T > 0:
        if S == 2:
            plot.setpos(x+L,y)
            T = 3
            print S
            
            plot.goto(x + L + L/q,y + h)
            plot.goto(x+L,y)
            plot.setpos(x+L+L/m,y)
            if x == 0 and y == 0 :
                x = x + L+ L/m
            else:
                x = x - L/q + L
                y = y + h
            print S
            if S == 1:
                plot.setpos(x+L/m,y+2*h)
                T = 3
                print S
            else:
                plot.setpos(x+L/m,y)

        else:
            #plot.setpos(x+L/2,y)
            while T > 0:
                plot.setpos(x+L/2,y)
                plot.goto(x + L/q,y + h)
                plot.goto(x,y)
                plot.setpos(x+L/m,y)
                if x == 0 and y == 0 :
                    x = x + L/2
                else:
                    x = x - L/4
                    y = y + h
                T = T - 1
            x = 0
            y = 0
            S = S - 1
        T = 3







    print h


    background.exitonclick() #close background
draw_plotter()
