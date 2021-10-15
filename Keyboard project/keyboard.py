import time
import random
import pyperclip
import keyboard

def foo():
    k=0.1
    f=[]

    #pyperclip.copy("# сейчас это в буфере обмена так как я туда скопировал")
    v = pyperclip.paste()
    print(v)
    for c in v:
        l = random.randint(1, 10) 
        k=l/ 100
        f.append(k)
        time.sleep(k)
        
        keyboard.write(c)
    print(f)
while True:
    keyboard.wait('Ctrl + \\')
    foo()
