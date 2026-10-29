"""from turtle import *

color("red", "yellow")
begin_fill()
forward(200)
left(120)
forward(200)
left(120)
forward(200)
end_fill()
done()"""


"""import turtle

t = turtle.Turtle()
mycolours = ["pink", "white", "purple"]
r= 25
n = 7
for i in range(n+1, 0, -1):
    t.color("brown", mycolours[i%3])
    t.begin_fill()
    t.circle(r*i)
    t.end_fill() """


""" import turtle

def draw(sides, length):
    ang = 360/sides
    colouing= ["red"]
    turtle.color("blue", colouing[0])
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(length)
        turtle.left(ang)
    turtle.end_fill()
        
        
s= int(input("enter num of sides:"))
l= int(input("enter side length:"))
draw(s,l)
turtle.done() """



