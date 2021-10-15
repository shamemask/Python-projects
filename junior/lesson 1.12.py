import turtle

t = turtle.Turtle()

def square():
    for i in range(4):
        t.forward(100)
        t.left(90)

def move(x,y):
    t.up()
    t.goto(x, y)
    t.down()

#square()
#move(-150,0)
#square()

def pentagon():
    for i in range(5):
        t.forward(100)
        t.left(72)
#move(150,-150)
#pentagon()

def polygon(sides):
    for i in range(sides):
        t.forward(50)
        t.left(360/sides)

#move(150,150)
#polygon(6)
#move(-150,150)
#polygon(9)
#move(-150,-150)
#polygon(12)

t.speed(10)
t.shape("turtle")

for i in range(24):
    polygon(10)
    t.left(15)

move(-220,-220)

for i in range(10):
    polygon(6)
    t.left(36)

move(200,200)

for i in range(6):
    polygon(4)
    t.left(60)

move(200,-200)

for i in range(6):
    polygon(7)
    t.left(60)

move(-200,200)

for i in range(60):
    polygon(5)
    t.left(6)

def circle():
    for i in range(60):
        t.forward(10)
        t.left(6)

move(0,0)
circle()

t.screen.mainloop()
