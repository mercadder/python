import turtle #module that draw things
import math
def draw_triangles():
    turtle.setworldcoordinates(-50, -50, 800, 800)
    background = turtle.Screen() #create the background
    background.bgcolor ("#005ce6") #background color
    
    pa = turtle.Turtle()
    pa.shape("arrow")
    pa.color("red","white")
    pa.speed(200)
    pa.penup()
    L = 100 #small triangle side
    l = 100 #same original L value
    h = math.sqrt((l)**2-(l/2)**2) #height small triangle
   
    a = 0 #origin horizontal coordinate
    b = 0 #origin vertical coordinate
    e = 2 #to set an even number
    n = 3 #triangle counter (is 3)
    N = 7 #counter of levels
    t = [[a,b],[L,b],[L/e,h]]
    pa.setpos(a,b)
    
    while N > 0:
        pa.pendown()
        pa.setpos(a,b)
        pa.goto(t[1][0],t[1][1])
        pa.goto(t[2][0],t[2][1])
        pa.goto(a,b)
        if n % 2 != 0:
            e = e*2
            a = L
            b = h
        else:
            a = L/e
            b = 2*h
        n = n - 1
        L = L*2
        h = h*2
        N = N - 1
    background.exitonclick() #close background
draw_triangles()
