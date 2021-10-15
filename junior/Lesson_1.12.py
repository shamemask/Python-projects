'''
import turtle 

t = turtle.Turtle()
t.up()
t.goto(-150, 150)
t.down()
for i in range(12):
    for j in range(4):
        t.forward(100)
        t.left(90)
    t.left(30)
t.screen.exitonclick()
'''
import turtle as t
t.shape("turtle")
t.speed(1000)

#Нарисовать квадрат
def draw_square():
    for i in range(4):
        t.forward(100)
        t.left(90)

#Нарисовать квадраты
def draw_squares():
    for i in range(12):
        draw_square()
        t.left(30)

#Нарисовать пятиугольник
def draw_polygon(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        t.forward(70)
        t.left(angle)

#Нарисовать круг
def draw_circle():
    for i in range(24):
        t.forward(15)
        t.left(15)

#Двигать указатель
def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

#Запуск функций
move(-200, 150)
draw_square()
move(-150, 0)
draw_squares()
move(150,0)
draw_polygon(10)
move(0, 150)
draw_circle()
t.screen.exitonclick()
