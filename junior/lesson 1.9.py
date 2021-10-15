import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm

window = tk.Tk()
window.geometry("400x400")
window.title("Мой блокнот")

file_name = "" 

def open_file():
    content = content_text.get(1.0, "end") 
    content_text.delete(1.0, "end") 
    global file_name
    
    file_name = tk.filedialog.askopenfilename() 
    with open(file_name, encoding="utf-8") as file:
        #print(file_name)
        print(file.read())
        s = file.read()
        content_text.insert(1.0, file.read() ) 
        
def save_as_file(): 
    global file_name 
    file_name = tk.filedialog.asksaveasfilename() 
    content = content_text.get(1.0, "end") 
    with open(file_name+".txt", "w", encoding="utf-8") as file: 
        file.write(content) 

def new_file(): 
    global file_name 
    if tkm.askokcancel("Создание нового файла", "Вы уверены? Несохраненный текст будет удален"): 
        file_name==""
        content = content_text.get(1.0, "end") 
        content_text.delete(1.0, "end") 
        
        with open(file_name+".txt", "w") as file: 
            file.write(content)
    
def save_file(): 
    global file_name
    
    content = content_text.get(1.0, "end") 
    with open(file_name+".txt", "w") as file: 
            file.write(content)   
    
content_text = tk.Text(window,bg="darkgreen", fg='white', wrap="word")
content_text.pack()
content_text.place(x=0,y=0,relwidth=1, relheight=1)
main_menu = tk.Menu(window)
window.configure(menu=main_menu)
frame = tk.Frame()
frame.pack()
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Файл", menu=file_menu)

new_file_icon = tk.PhotoImage(file="C:/Users/dartamonov/Documents/Git/Python/Python/junior/icons/new_file.gif")
open_file_icon =tk.PhotoImage(file="C:/Users/dartamonov/Documents/Git/Python/Python/junior/icons/open_file.gif")
save_file_icon = tk.PhotoImage(file="C:/Users/dartamonov/Documents/Git/Python/Python/junior/icons/save_file.gif")


file_menu.add_command(label="Новый", image=new_file_icon, compound="left", command=new_file)
file_menu.add_command(label="Открыть", image=open_file_icon, compound="left", command = open_file)
file_menu.add_command(label="Сохранить", image=save_file_icon, compound="left", command = save_file)
file_menu.add_command(label="Сохранить как", image=save_file_icon, compound="left", command=save_as_file)

file_label = tk.Label(window, text = "Файл: "+file_name)
file_label.place(relx=0, rely=1, anchor="sw")

window.mainloop()