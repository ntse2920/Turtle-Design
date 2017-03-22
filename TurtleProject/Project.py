from myFunction import *
import turtle
a=turtle.Turtle()
b=turtle.Turtle()
d=turtle.Turtle()
e=turtle.Turtle()
f=turtle.Turtle()
g=turtle.Turtle()
h=turtle.Turtle()
i=turtle.Turtle()
j=turtle.Turtle()
k=turtle.Turtle()
l=turtle.Turtle()

a.speed(0)
b.speed(0)
d.speed(0)
e.speed(0)
f.speed(0)
g.speed(0)
h.speed(0)
i.speed(0)
j.speed(0)
k.speed(0)
l.speed(0)
turtle.colormode(255)
turtle.bgcolor("black")

#Blue shape made by combining five pentagons.
for times in range(4):
    c=(times,times,times)
    a.color("blue")
    print(c)
    jump(a,-275,275)
    shape(a)
jump(b,-300,225)
#Blue lines making a pattern.
for times in range(3):
    b.color("blue")
    print(c)
    line(b)
b.right(90)
b.forward(450)
#Green shape made by combining five pentagons.
for times in range(4):
    c=(0,255,0)
    d.color(c)
    print(c)
    jump(d,-275,-275)
    shape(d)
e.color(c)
print(c)
jump(e,-225,-300)
#Green lines making a pattern
for times in range(3):
    lines(e)
e.forward(450)
#Red shape made by combining five pentagons.
for times in range(4):
    jump(f,275,-275)
    f.color("red")
    c=(0,0,255)
    print(c)
    shape(f)
g.penup()
g.goto(250,225)
g.pendown()
#Red lines making a pattern.
for times in range(3):
    g.color("red")
    line(g)
g.right(90)
g.forward(450)
#Yellow shape made by combining five pentagons.
for times in range(4):
    jump(h,275,275)
    h.color("yellow")
    shape(h)
i.penup()
i.goto(-225,250)
i.pendown()
for times in range(3):
    i.color("yellow")
    lines(i)
i.forward(450)
#Makes a white circle.
for times in range(100):
    j.color("white")
    j.circle(100)
    j.left(5)
    j.width(2)
#makes a star changing from white to black.
for times in range(255):
    k.width(5)
    c=(255-times,255-times,255-times)
    k.color(c)
    print(c)
    polygon(k,1,1)
    k.left(145)
    k.forward(times)
l.color("gray")
jump(l,175,200)
#Makes gray design out of gray squares. 
for times in range(4):
    shapes(l)
    c=(255-times,times,times)
jump(l,175,-175)
#Makes gray design out of gray squares. 
for times in range(4):
    shapes(l)
    c=(times,25-times,times)
jump(l,-180,200)
#Makes gray design out of gray squares. 
for times in range(4):
    shapes(l)
    c=(times,times,255-times)
jump(l,-180,-175)
#Makes gray design out of gray squares. 
for times in range(4):
    shapes(l)

    
    
    

   
    


