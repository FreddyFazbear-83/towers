import tkinter as tk
import random
from PIL import ImageTk, Image

class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")

        self.towers = []
        for i in range(3):
            tower_image = ImageTk.PhotoImage(Image.open("wer.jpg"))
            tower_button = tk.Button(root, image=tower_image, command=lambda idx=i: self.attack_enemy(idx))
            tower_button.health = 100
            tower_button.image = tower_image
            tower_button.place(x=10, y=150*i+50)
            self.towers.append(tower_button)

        # Create enemies
        self.enemies = []
        for _ in range(5):
            self.create_enemy()

        self.destroyed_towers = 0

        self.create_red_square()

    def attack_enemy(self, tower_idx):
        tower_button = self.towers[tower_idx]
        tower_button.health -= 25
        if tower_button.health <= 0:
            tower_button.destroy()
            self.destroyed_towers += 1
            if self.destroyed_towers == 5:
                self.create_new_tower_button()

        if tower_button.image == self.towers[0].image:
            self.attack_red_square()

    def attack_red_square(self):
        self.red_square.health -= 25
        if self.red_square.health <= 0:
            self.red_square.red_square.destroy()

    def create_new_tower_button(self):
        new_tower_button = tk.Button(self.root, image=self.towers[0].image, command=lambda: self.attack_enemy(0))
        new_tower_button.place(x=400, y=300)
        self.towers[0] = new_tower_button

    def create_enemy(self):
        enemy = Enemy(self.root, x=700, y=random.randint(50, 450))
        self.enemies.append(enemy)
        enemy.move_enemy()

    def create_red_square(self):
        self.red_square = RedSquare(self.root, x=100, y=100)

class Enemy:
    def __init__(self, root, x, y):
        self.root = root
        self.health = 100
        self.speed = 5
        self.direction = -1

        self.enemy_image = ImageTk.PhotoImage(Image.new("RGB", (30, 30), "red"))
        self.enemy_button = tk.Button(root, image=self.enemy_image, command=self.destroy_enemy)
        self.enemy_button.place(x=x, y=y)

        self.health_label = tk.Label(root, text=str(self.health), bg="white")
        self.health_label.place(x=x, y=y+35)

    def move_enemy(self):
        self.root.after(100, self.move_helper)

    def move_helper(self):
        x = self.enemy_button.winfo_x()
        if x <= 0:
            self.destroy_enemy()
            return
        self.enemy_button.place(x=x + self.direction * self.speed, y=self.enemy_button.winfo_y())
        self.health_label.place(x=x + self.direction * self.speed, y=self.enemy_button.winfo_y() + 35)
        self.root.after(100, self.move_helper)

    def destroy_enemy(self):
        self.enemy_button.destroy()
        self.health_label.destroy()

class RedSquare:
    def __init__(self, root, x, y):
        self.root = root
        self.health = 100

    def attack(self):
        self.health -= 25
        if self.health <= 0:
            self.red_square.destroy()

root = tk.Tk()
app = Window(root)
root.mainloop()
