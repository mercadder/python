import turtle #module that draw things
import math

def draw_plotter():
    turtle.setworldcoordinates(-200, -200, 1000, 1000)
    background = turtle.Screen() #create the background
    background.bgcolor ("#005ce6") #background color
    
    plot = turtle.Turtle()
    plot.shape("arrow")
    plot.color("red","white")
    plot.speed(50)
    x = 0
    y = 0
    T = 4 #triangle, counter backward
    R = T #counter forward
    L = 100 #length of side
    h = math.sqrt((L)**2-(L/2)**2) #height small triangle
    n = 0 #level counter
    plot.up()
    #plot.setpos(x+L,y)
    plot.down()
    I = T #number of interaction
    c = "red"
    d = "green"
    plot.begin_fill()
    
    while I > 0:
        n = n + 1
        while T > 0:
            plot.up()
            plot.setpos(x+L,y)
            plot.down()
            if n == 2:
                plot.end_fill()
            else:
                plot.begin_fill()
            plot.setpos(x,y)
            plot.left(60)
           
        
            plot.forward(L)
            plot.color(d, c)
            plot.right(120)
            plot.forward(L)
           
            plot.left(60)
            plot.color(c, d)
            x = x + L
            
            T = T - 1
                    #else:
         
        T = R - n
        
        x = L/2*n
        
        y = h*(n)
        
        I = I - 1
        plot.end_fill()

    background.exitonclick() #close background
draw_plotter()
