import tkinter as tk
import tkinter.messagebox as tmb
import random

window = tk.Tk()
window.title("Угадай cлово")
window.geometry("300x200")

with open("junior\words.txt") as file:
    data = file.read()

words = data.split()
print(words)