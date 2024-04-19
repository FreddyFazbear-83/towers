import tkinter as tk
import random

class GameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Простая игра")
        self.master.geometry("600x400")

        self.canvas = tk.Canvas(self.master, width=600, height=400, bg="white")
        self.canvas.pack()

        # Зеленый квадрат - игрок
        self.player = self.canvas.create_rectangle(50, 175, 100, 225, fill="green")

        # Характеристики игрока
        self.player_health = 100
        self.player_health_display = self.canvas.create_text(50, 50, text=f"Здоровье: {self.player_health}", anchor="nw")

        # Боты-враги
        self.enemies = []
        self.enemy_health = 100
        self.enemy_health_display = self.canvas.create_text(500, 50, text=f"Здоровье врага: {self.enemy_health}", anchor="nw")

        # Создание кнопки для стрельбы
        self.fire_button = tk.Button(self.master, text="Стрелять", command=self.fire_bullet)
        self.fire_button.pack()

    def fire_bullet(self):
        # Пуля вылетает с зеленого квадрата
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle(x2, y1+50, x2+20, y2-50, fill="red")

        # Проверка попадания пули во врага
        for enemy in self.enemies:
            if self.canvas.bbox(bullet) and self.canvas.bbox(enemy) and self.canvas.bbox(bullet, enemy):
                self.canvas.delete(bullet)
                self.enemy_health -= 25
                self.canvas.itemconfig(self.enemy_health_display, text=f"Здоровье врага: {self.enemy_health}")
                if self.enemy_health <= 0:
                    self.canvas.delete(enemy)
                    self.enemies.remove(enemy)
                    self.enemy_health = 100
                    self.canvas.itemconfig(self.enemy_health_display, text=f"Здоровье врага: {self.enemy_health}")
                    break

        # Движение пули
        self.canvas.move(bullet, 10, 0)
        self.master.after(100, lambda: self.check_bullet(bullet))

    def check_bullet(self, bullet):
        # Проверка, вышла ли пуля за пределы холста
        if self.canvas.coords(bullet)[2] >= 600:
            self.canvas.delete(bullet)

    def spawn_enemy(self):
        # Создание бота-врага
        enemy = self.canvas.create_rectangle(550, random.randint(100, 300), 600, random.randint(100, 300), fill="purple")
        self.enemies.append(enemy)
        self.master.after(2000, self.spawn_enemy)

root = tk.Tk()
app = GameApp(root)
app.spawn_enemy()
root.mainloop()