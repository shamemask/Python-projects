import time
import tkinter as tk
#import tkinter.messagebox as tmb
import random
import recogen as recog

window = tk.Tk()
window.title("Назови цвет")
window.geometry("500x250")

# words = ['красный', "синий", "зелёный", "розовый", "чёрный",
#         "жёлтый", "оранжевый", "фиолетовый", "коричневый"]
words = ["red", "blue", "green", "pink", "black",
         "yellow", "orange", "purple", "brown"]

colors = ["red", "blue", "green", "pink", "black",
          "yellow", "orange", "purple", "brown"]
score = 0
fails = 0
time_left = 10


def timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label["text"] = f"Осталось секунд: {time_left}"
        time_label.after(1000, timer)
    ''' ДЗ
    else:
        tmb.showinfo("Конец игры", "Время вышло")
    '''


def new_word():
    color_label["fg"] = random.choice(colors)
    color_label["text"] = random.choice(words)


def check(event):
    global score
    global fails
    if time_left > 0:
        word_color = color_label["fg"]
        i = colors.index(word_color)
        color = words[i]
        response = recog.speech()
        print(color, response)
        if color == response:
            print("да")
            score += 1
            score_label["text"] = f"Правильно: {score}"
        else:
            print("нет")
            fails += 1
            fails_label["text"] = f"Неправильно: {fails}"
        new_word()


instructions = tk.Label(
    window, text="Введи цвет слова, а не слово! Жми Enter, чтобы играть.", font=("Helvetica", 10))
instructions.place(x=10, y=10)

score_label = tk.Label(
    window, text=f"Правильно: {score}", font=("Helvetica", 10))
score_label.place(x=10, y=40)

fails_label = tk.Label(
    window, text=f"Неправильно: {fails} ", font=("Helvetica", 10))
fails_label.place(x=10, y=60)

color_label = tk.Label(window, text=random.choice(
    words), font=("Helvetica", 60))
color_label.place(x=10, y=80)

time_label = tk.Label(window, text=f"Осталось секунд: {time_left}")
time_label.place(x=10, y=210)

new_word()

window.bind('<Return>', check)
time_label.after(1000, timer)
window.mainloop()
