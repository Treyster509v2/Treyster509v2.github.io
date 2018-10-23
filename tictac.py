import turtle

def tictak(t):
    # *******************
    t.penup()
    t.goto(-150,50)
    t.pendown()
    t.goto(150,50)
    t.penup()
    t.goto(-150,-50)
    t.pendown()
    t.goto(150,-50)

    t.penup()
    t.goto(-50,150)
    t.pendown()
    t.goto(-50,-150)
    t.penup()
    t.goto(50,150)
    t.pendown()
    t.goto(50,-150)


def circle(t,x,y,size,tcolor):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(tcolor)
    t.circle(size)

def make_x(t,x,y,size,tcolor):
    t.penup()
    t.goto(x,y)
    t.seth(0)
    t.pendown()
    t.color(tcolor)
    t.right(45)
    t.forward(size)
    t.back(size/2)
    t.left(90)
    t.forward(size/2)
    t.back(size)


def gameboard():
    tw = turtle.Screen()
    tw.clear()
    t = turtle.Turtle()
    t.width(3)
    t.speed(0)
    tictak(t)
    # circle def circle(t,x,y,size,tcolor):
    tcolor = "#ff0000"
    circle(t,-75,75,25,tcolor)
    tcolor = "#00ff00"
    circle(t,0,75,25,tcolor)
    tcolor = "#0000ff"
    circle(t,75,75,25,tcolor)
    tcolor = "#ff00ff"
    circle(t,-75,0,25,tcolor)
    tcolor = "#00ffff"
    circle(t,0,0,25,tcolor)

    #make x def make_x(t,x,y,size,tcolor):
    tcolor = "#ff0000"
    make_x(t,-20,-60,60,tcolor)
    tcolor = "#00ff00"
    make_x(t,-100,-50,60,tcolor)
    tcolor = "#0000ff"
    make_x(t,70,40,60,tcolor)
    tcolor = "#ff00ff"
    make_x(t,75,-60,60,tcolor)

    tw.exitonclick()

gameboard()
