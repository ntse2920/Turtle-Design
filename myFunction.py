def tear(t):
    for times in range(10):
        t.circle(times * 2)
        t.left(10)
        t.forward(10)
        
def L(t,distance,angle):
    t.forward(distance)
    t.left(angle)
    t.forward(distance)
    

def polygon(t, sides, distance):
    angle = 360 / sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def cool(t):
    t.color("blue")
    polygon(t,5,100)
    t.color("black")
    polygon(t,4,100)
    t.color("orange")
    polygon(t,3,100)

def coolsquare(t):
    for times in range(4):
        cool(t)
        t.right(90)

def jump(t,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

#Makes shape out of 4 pentagons
def shape(t):
    polygon(t,5,25)
    t.forward(50)
    t.right(90)

#Makes shape out of 4 squares
def shapes(t):
    polygon(t,4,25)
    t.forward(25)
    t.right(90)

#Makes vertical line pattern
def line(t):
    t.right(90)
    t.forward(450)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(450)
    t.right(90)
    t.forward(10)

#Makes horizontal line pattern
def lines(t):
    t.forward(450)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(450)
    t.right(90)
    t.forward(10)
    t.right(90)

