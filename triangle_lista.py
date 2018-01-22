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
    
    L = 100 #small triangle side
    h = math.sqrt((L)**2-(L/2)**2) #height small triangle
    print (h)
    a = 0 #origin horizontal coordinate
    b = 0 #origin vertical coordinate
    e = 2 #even number
    n = 1 #triangle counter
    t = [[a,b],[L,b],[L/e,h]]
         
         #pa.setpos(t[0][0],t[0][1])
    background.exitonclick() #close background
draw_triangles()
         
