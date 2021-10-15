import tkinter as tk 
import tkinter.messagebox as tmb
import random 

window = tk.Tk() 
window.title("Угадай cлово") 
window.geometry("300x200") 

with open("C:/Users/dartamonov/Documents/Git/Python/Python/junior/words.txt", encoding="utf-8") as file: 
    data = file.read() 

words = data.split() 
word = random.choice(words)
shuffle=''.join(random.sample(word, len(word)))
letters = []
attempts = 10

def new_game(): 
    global word
    global letters
    global attempts
    attempts = 10
    label_attempts["text"] = f"У тебя осталось {attempts} попыток"
    letters = [] 
    word = random.choice(words) 
    shuffle=''.join(random.sample(word, len(word)))
    label_word["text"] = f"Здесь будет слово \n{shuffle}" 


def check_letter(): 
    letter = entry_letter.get() 
    letters.append(letter)
    entry_letter.delete(0, "end")
    print(letter)

    show_word = "" 

    for char in word:
        if char in letters: 
            show_word += char 
        else: 
            show_word += "*"
    label_word["text"] = f"Здесь будет слово \n{shuffle}\n{show_word}"
    if show_word == word: 
        print("Победа!!!")
        tmb.showinfo("Победа", "Ты угадал слово!")
        new_game()
    if letter not in word:
        attempts-=1
        label_attempts["text"] = f"У тебя осталось {attempts} попыток"
        if attempts==0:
            tmb.showinfo("Проигрыш", f"Ты не угадал слово! Слово было - {word}")
            new_game()


label_word = tk.Label(window, text=f"Здесь будет слово \n{shuffle}", font=("Arial", 15))
label_word.place(x=70, y=20)

entry_letter = tk.Entry(window, width=8, font=("Arial", 10)) 
entry_letter.place(x=130, y=110) 

check_button = tk.Button(window, text="Проверить букву", font=("Arial", 10), command = check_letter)
check_button.place(x=100, y=150)

label_attempts = tk.Label(window, text=f"У тебя осталось {attempts} попыток", font=("Arial", 10))
label_attempts.place(x=70, y=180)



window.mainloop() 