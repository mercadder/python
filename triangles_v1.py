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
    T = 7 #triangle sides, counter
    R = T
    L = 100 #length of side
    h = math.sqrt((L)**2-(L/2)**2) #height small triangle
    n = 0 #level counter
    plot.up()
    #plot.setpos(x+L,y)
    plot.down()
    I = 7 #number of interaction
    
    
    while I > 0:
        n = n + 1
        while T > 0:
            plot.up()
            plot.setpos(x+L,y)
            plot.down()
            plot.setpos(x,y)
            plot.left(60)
            plot.forward(L)
            plot.right(120)
            plot.forward(L)
            plot.left(60)
            x = x + L
            T = T - 1
        x = L/2
        y = h
       
        T = R - n
        print T
        print n
        y = h
        
        I = I - 1





    print h


    background.exitonclick() #close background
draw_plotter()
