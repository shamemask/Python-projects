import tkinter as tk
import random
import time

colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'Purple', 'Brown']

stop = False


def draw_circle():
    color = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500-d)
    y = random.randint(0, 500-d)


    canvas.create_oval(x, y, x + d, y + d, fill=color)


def draw_oval():
    color = random.choice(colors)
    d1 = random.randint(1, 100)
    d2 = random.randint(1, 100)
    x = random.randint(0, 500-d1)
    y = random.randint(0, 500-d2)

    canvas.create_oval(x, y, x + d1, y + d2, fill=color)


def draw_square():
    color = random.choice(colors)
    color_border = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500-d)
    y = random.randint(0, 500-d)


    canvas.create_rectangle(x, y, x + d, y + d, fill=color, outline=color_border)


def draw_circles():
    global stop
    while True:
        draw_circle()
        window.update()
        time.sleep(0.5)
        if stop:
            stop = False
            break
''' ДЗ
def draw_squares():
    global stop
    while True:
        draw_square()
        window.update()
        time.sleep(1)
        if stop:
            stop = False
            break
'''
def stop_draw():
    global stop
    stop = True


def animate_circle():
    #global stop ДЗ
    color = random.choice(colors)
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    d = random.randint(0, 100)

    circle = canvas.create_oval(x, y, x + d, y + d, fill=color)

    dx = 1
    dy = 1
    while True:
        canvas.move(circle, dx, dy)
        time.sleep(0.01)
        window.update()

        coords = canvas.coords(circle)
        print(coords)
        left = coords[0]
        top = coords[1]
        right = coords[2]
        bottom = coords[3]

        if left <= 0 or right >= 500:
            dx = -dx
        if top <= 0 or bottom >= 500:
            dy = -dy

        canvas.move(circle, dx, dy)
        time.sleep(0.025)
        window.update()
        ''' ДЗ
        if stop:
            stop = False
            break
        '''

window = tk.Tk()
window.title("Цветные фигуры")
window.geometry("650x500")

canvas = tk.Canvas(window, bg="white", width=500, height=500)

canvas.place(x=0, y=0)

button_circle = tk.Button(window, text="Нарисовать круг", width=17, command=draw_circle)
button_circle.place(x=510, y=20)

button_oval = tk.Button(window, text="Нарисовать овал", width=17, command=draw_oval)
button_oval.place(x=510, y=90)

button_square = tk.Button(window, text="Нарисовать квадрат", width=17, command=draw_square)
button_square.place(x=510, y=150)

button_circles = tk.Button(window, text="Бесконечные круги", width=17, command=draw_circles)
button_circles.place(x=510, y=220)

button_circle_a = tk.Button(window, text="Анимировать круг", width=17, command=animate_circle)
button_circle_a.place(x=510, y=290)

stop_button = tk.Button(window, text="Остановить анимацию", bg="orange", width=17, command=stop_draw)
stop_button.place(x=510, y=360)

''' ДЗ
button_squares = tk.Button(window, text="Бесконечные квадраты", width=17, command=draw_squares)
button_squares.place(x=510, y=410)
'''
window.mainloop()
