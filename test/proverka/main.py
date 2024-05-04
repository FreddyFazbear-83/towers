import tkinter as tk
import random

class TowerDefenseGame:
    def __init__(self, master):
        self.master = master
        self.master.attributes('-fullscreen', True)

        self.canvas = tk.Canvas(self.master, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.enemies = []
        self.spawn_enemy()

        self.text_box = TextBox(self.canvas, "В данный момент контент не доступен. можете полюбоваться этим или уходите  -->")
        self.text_box.display_message()

        self.btn_exit = tk.Button(self.canvas, text="Вернуться в главное меню", font=("Courier New", 15), bg="black", fg="red", command=self.canvas.destroy)
        self.btn_exit.place(x=1100, y=25)

    def spawn_enemy(self):
        enemy = Enemy(self.canvas)
        self.enemies.append(enemy)
        self.master.after(300, self.spawn_enemy)

class Enemy:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(1700, random.randint(250, 750), 1710, random.randint(100, 900), fill=random.choice(["aqua","dark violet", "crimson", "chartreuse2", "yellow", "darkorange2","deeppink1", "seagreen1","blue2"]))
        self.move()

    def move(self):
        self.canvas.move(self.id, -1, 0)
        if self.canvas.coords(self.id)[2] <= 0:
            self.canvas.coords(self.id, 1700, random.randint(550, 950), 1750, random.randint(100, 900))
            self.canvas.itemconfig(self.id, fill=random.choice(["aqua", "deepskyblue", "chartreuse2", "yellow", "darkorchid1","deeppink1"]))
        else:
            self.canvas.after(10, self.move)

class TextBox:
    def __init__(self, canvas, message):
        self.canvas = canvas
        self.message = message
        self.text_id = None

    def display_message(self):
        self.text_id = self.canvas.create_text(500, 50, text='', fill='white', font=('Courier New', 15))
        self.animate_text()

    def animate_text(self, index=0):
        if index < len(self.message):
            self.canvas.itemconfig(self.text_id, text=self.message[:index+1])
            self.canvas.after(100, self.animate_text, index+1)

def main():
    root = tk.Tk()
    game = TowerDefenseGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()