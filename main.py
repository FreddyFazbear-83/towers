from tkinter import *
from tkinter import Button
import tkinter as tk


#def finish():
   # root.destroy()  # ручное закрытие окна и всего приложения
    #print("Закрытие приложения")

root = tk.Tk()
#root['background']='black'


root.title("glory to the kihg")
root.iconbitmap(default="king.ico")
root.geometry("1450x856") #650x250
#root.attributes("-fullscreen", True)
#открытие программы без точек входа и выхода






#выход
button = Button(root, text="выход",
            command = root.destroy)

button.pack(side = 'top')
button.pack(pady=45)
button.config(fg="red", bg="black", font=("Courier New", 25))










root.mainloop()

