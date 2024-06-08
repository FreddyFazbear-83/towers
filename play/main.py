import tkinter as tk
import random
from PIL import ImageTk, Image
import datetime
from tkinter import messagebox
#музыка
import pyaudio
import wave
import threading


class Music:
    def __init__(self):
        self.is_playing = threading.Event()
        self.is_playing.set()

    def play_music(self, file_path):
        def play_stream():
            while self.is_playing.is_set():
                wf = wave.open(file_path, 'rb')
                p = pyaudio.PyAudio()
                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)
                data = wf.readframes(1024)
                while data != b'':
                    stream.write(data)
                    data = wf.readframes(1024)
                stream.stop_stream()
                stream.close()
                p.terminate()

        self.music_thread = threading.Thread(target=play_stream)
        self.music_thread.daemon = True
        self.music_thread.start()

    def stop_music(self):
        self.is_playing.clear()

music_player = Music()
music_player.play_music("new .wav")

class Window:
    def __init__(self, root, music_player):
        self.root = root
        self.music_player = music_player
        self.root.attributes('-fullscreen', True)
        self.is_game_over = False
        self.score = 0
        self.couns = 0
        self.score_label = tk.Label(root, text="- количество побеждённых врагов: 0")
        self.score_label.place(x=250, y=10)
        self.couns_label = tk.Label(root, text="0")
        self.couns_label.place(x=715, y=10)
        self.destroyed_towers = 0

#интерфейс игры
        self.background_img = ImageTk.PhotoImage(Image.open("obou3.jpg"))
        self.background_label = tk.Label(self.root, image=self.background_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.exit = ImageTk.PhotoImage(Image.open("exit.jpg"))
        self.btn_exit = tk.Button(self.root, image=self.exit,bg="black", command=self.root.destroy)
        self.btn_exit.place(x=114, y=632)

        self.enemy_ded = ImageTk.PhotoImage(Image.open("enemy.jpg"))
        self.btn_enemy_ded = tk.Button(self.root, image=self.enemy_ded, bg="black", command=self.view_scores)
        self.btn_enemy_ded.place(x=115, y=10)

        # Создаем квадрат для couns
        self.info_frame = tk.Frame(self.root, width=80, height=80, bg="black")
        self.info_frame.place(x=1038, y=631)
        self.info_img = ImageTk.PhotoImage(Image.open("couns.jpg"))
        self.info_label = tk.Label(self.info_frame, image=self.info_img)
        self.info_label.place(x=0, y=0)

        self.exit_bar = tk.Label(self.root, bg="black", width=7, height=9)
        self.exit_bar.place(x=351, y=633)
        self.exit1_bar = tk.Label(self.root, bg="black", width=3, height=9)
        self.exit1_bar.place(x=110, y=633)
        self.exit2_bar = tk.Label(self.root, bg="black", width=40, height=1)
        self.exit2_bar.place(x=110, y=633)

        self.couns_bar = tk.Label(self.root, bg="#FFF", width=44, height=5)
        self.couns_bar.place(x=1038, y=700)

        self.floor_bar = tk.Label(self.root, bg="#FFF", width=1700, height=10)
        self.floor_bar.place(x=0, y=772)

        self.fgreen_bar = tk.Label(self.root, bg="#FFF", width=15, height=600)
        self.fgreen_bar.place(x=0, y=0)

        self.fwrit_bar = tk.Label(self.root, bg="#FFF", width=17, height=600)
        self.fwrit_bar.place(x=1345, y=0)

        self.root = root
        self.restart = ImageTk.PhotoImage(Image.open("restart.jpg"))
        self.btn_restart = tk.Button(self.root, image=self.restart, bg="black", command=self.reset_app)
        self.btn_restart.place(x=447, y=632)

        self.zamokobou = ImageTk.PhotoImage(Image.open("zamokobou.jpg"))
        self.btn_zamokobou = tk.Button(self.root, image=self.zamokobou, bg="black", command=self.place_zamokobou)
        self.btn_zamokobou.place(x=745, y=632)

    def update_couns_display(self):
        self.couns_label.config(text=str(self.couns))

    def place_tower(self, event):
        if self.couns >= 50 and self.root.cget("cursor") == "plus":
            self.couns -= 50
            self.update_couns_display()
            # Размещаем башню
            tower = Tower(self.root, event.x, event.y, self.enemies)
            tower.shoot()
            tower.destroy_enemy_if_hit()

            # Возвращаем курсор в первоначальный вид
            self.root.config(cursor='arrow')
            # Отвязываем событие от нажатия кнопки мыши
            self.root.unbind('<Button-1>')

    def place_zamokobou(self):
        if self.root.cget("cursor") == "plus":
            self.root.config(cursor='arrow')
        else:
            self.root.config(cursor='plus')
        self.root.bind('<Button-1>', self.place_tower)

    def reset_app(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.background_img = ImageTk.PhotoImage(Image.open("obou3.jpg"))
        self.background_label = tk.Label(self.root, image=self.background_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Воспроизведение музыки
        self.music_player.stop_music()  # Останавливаем текущую музыку
        self.music_player.play_music("new .wav")

        self.restart = ImageTk.PhotoImage(Image.open("restart.jpg"))
        self.btn_restart = tk.Button(self.root, image=self.restart, bg="black", command=self.reset_app)
        self.btn_restart.place(x=447, y=632)

        self.zamokobou = ImageTk.PhotoImage(Image.open("zamokobou.jpg"))
        self.btn_zamokobou = tk.Button(self.root, image=self.zamokobou, bg="black", command=self.place_zamokobou)
        self.btn_zamokobou.place(x=745, y=632)

        self.exit = ImageTk.PhotoImage(Image.open("exit.jpg"))
        self.btn_exit = tk.Button(self.root, image=self.exit, bg="black", command=self.root.destroy)
        self.btn_exit.place(x=115, y=632)

        self.enemy_ded = ImageTk.PhotoImage(Image.open("enemy.jpg"))
        self.btn_enemy_ded = tk.Button(self.root, image=self.enemy_ded, bg="black", command=self.view_scores)
        self.btn_enemy_ded.place(x=115, y=10)

        self.is_game_over = False
        self.score = 0
        self.score_label = tk.Label(root, text="<- в конце игры не забудь нажать на эту кнопочку для сохранения твоего прогресса", fg="red", font=("Courier New", 10))
        self.score_label.place(x=171, y=10)
        self.couns = 0
        self.couns_label = tk.Label(root, text="0",bg="black", fg="yellow", font=("Courier New", 50))
        self.couns_label.place(x=1111, y=636)
        self.destroyed_towers = 0

        self.towers = []
        for i in range(0):
            tower_image = ImageTk.PhotoImage(Image.open("tower.jpg"))
            tower_button = tk.Button(root, image=tower_image, command=lambda idx=i: self.attack_enemy(idx))
            tower_button.health = 100
            tower_button.image = tower_image
            tower_button.place(x=130, y=200*i+90)
            self.towers.append(tower_button)

        self.enemies = []
        self.create_enemy()
        self.create_red_square()
        self.create_green_bar()

    def create_enemy(self):
        if not self.is_game_over and len(self.enemies) < 1000:  # Проверяем, не окончена ли игра и количество врагов
            x = random.randint(1300, 2450)
            y = random.randint(100, 550)
            enemy = Enemy(self.root, x, y, game_over_callback=self.check_game_over, score_callback=self.update_score, couns_callback=self.update_couns)
            self.enemies.append(enemy)
            enemy.move_enemy()
            if len(self.enemies) < 1000:  # Создаем нового врага, если их меньше 1000
                self.root.after(1000, self.create_enemy)
        self.writ_bar = tk.Label(self.root, bg="#FFF", width=17, height=600)
        self.writ_bar.place(x=1345, y=0)
        green_bar = tk.Label(self.root, bg="#FFF", width=15, height=600)
        green_bar.place(x=0, y=0)

    def create_red_square(self):
        self.red_square = RedSquare(self.root, x=100, y=100)

    def create_green_bar(self):
        green_bar = tk.Label(self.root, bg="#FFF", width=15, height=600)
        green_bar.place(x=0, y=0)
        self.green_bar = green_bar

        self.writ_bar = tk.Label(self.root, bg="#FFF", width=17, height=600)
        self.writ_bar.place(x=1345, y=0)

        exit_bar = tk.Label(self.root, bg="black", width=7, height=9)
        exit_bar.place(x=351, y=633)
        exit1_bar = tk.Label(self.root, bg="black", width=3, height=9)
        exit1_bar.place(x=110, y=633)
        exit2_bar = tk.Label(self.root, bg="black", width=40, height=1)
        exit2_bar.place(x=110, y=633)

        self.info_frame = tk.Frame(self.root, width=80, height=80, bg="black")
        self.info_frame.place(x=1038, y=631)
        self.info_img = ImageTk.PhotoImage(Image.open("couns.jpg"))
        self.info_label = tk.Label(self.info_frame, image=self.info_img)
        self.info_label.place(x=0, y=0)

        self.couns_bar = tk.Label(self.root, bg="#FFF", width=44, height=5)
        self.couns_bar.place(x=1038, y=700)

        floor_bar = tk.Label(self.root, bg="#FFF", width=1700, height=10)
        floor_bar.place(x=0, y=772)

    def view_scores(self):
        with open("scores.txt", "a") as file:
            score_entry = f"Очки: {self.score}, Дата: {datetime.datetime.now()}\n"
            file.write(score_entry)
        tk.messagebox.showinfo("Рекорды", f"""                   Ты умница!!
        Результат сохранен в файле""")

    def update_score(self, points):
        self.score += points
        self.score_label.config(text=f"- количество побеждённых врагов: {self.score} ", fg="black", font=("Courier New", 10))

    def qwerty(self):
        game_over_bar = tk.Label(self.root, bg="#FFF", width=176, height=37)
        game_over_bar.place(x=110, y=70)
        game_over_label = tk.Label(game_over_bar, text="Игра окончена", bg = "#FFF",fg="black", font=("Courier New", 50))
        game_over_label.place(x=400, y=200)
        score_label = tk.Label(game_over_bar, text=f"Очки за игру: {self.couns}",bg = "#FFF",fg="red", font=("Courier New", 20))
        score_label.place(x=400, y=300)
        couns_label = tk.Label(game_over_bar, text=f"Кол-во побеждённых врагов: {self.score}",bg = "#FFF",fg="red", font=("Courier New", 20))
        couns_label.place(x=400, y=350)
    def update_couns(self, points):
        self.couns += points * 10
        self.couns_label.config(text=f"{self.couns} ", bg="black", fg="yellow", font=("Courier New", 50))

    def check_game_over(self):  # Переименован метод
        if not self.is_game_over:  # Используем новое имя переменной
            self.is_game_over = True  # Устанавливаем флаг окончания игры
            game_over_bar = tk.Label(self.root, bg="#FFF", width=176, height=37)
            game_over_bar.place(x=110, y=70)
            game_over_label = tk.Label(game_over_bar, text="Игра окончена", bg="#FFF", fg="black",
                                       font=("Courier New", 50))
            game_over_label.place(x=400, y=200)
            couns_label = tk.Label(game_over_bar, text=f"Кол-во побеждённых врагов: {self.score}", bg="#FFF", fg="red",
                                   font=("Courier New", 20))
            couns_label.place(x=400, y=300)
            for enemy in self.enemies:  # Останавливаем всех врагов
                self.root.after_cancel(enemy.move_enemy)
class Enemy:
    def __init__(self, root, x, y, game_over_callback, score_callback, couns_callback):
        self.root = root
        self.health = 10
        self.speed = 5
        self.direction = -1
        self.game_over_callback = game_over_callback
        self.score_callback = score_callback
        self.couns_callback = couns_callback

        self.enemy_image = ImageTk.PhotoImage(Image.new("RGB", (40, 40), "red"))
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
            self.game_over_callback()
            return
        if x <= 60:
            self.game_over_callback()
            return
        # Изменяем направление на правильное
        self.enemy_button.place(x=x - self.speed, y=self.enemy_button.winfo_y())
        self.health_label.place(x=x - self.speed, y=self.enemy_button.winfo_y() + 35)
        self.root.after(100, self.move_helper)

    def destroy_enemy(self):
        # Проверяем, находится ли курсор в форме плюсика
        if self.root.cget("cursor") != "plus":
            self.enemy_button.destroy()
            self.health_label.destroy()
            self.score_callback(1)  # Засчитываем баллы только если курсор не в форме плюсика
            self.couns_callback(1)  # Засчитываем couns только если курсор не в форме плюсика
        else:
            # Если курсор в форме плюсика, просто убираем врага с экрана без засчитывания баллов
            self.enemy_button.place_forget()
            self.health_label.place_forget()

    def check_collision(self, bullet):
        if abs(self.enemy_button.winfo_x() - bullet.x) < 20 and abs(self.enemy_button.winfo_y() - bullet.y) < 20:
            self.destroy_enemy()
            bullet.bullet_label.destroy()
class RedSquare:
    def __init__(self, root, x, y):
        self.root = root
        self.health = 100

class Bullet:
    def __init__(self, root, x, y, enemies):
        self.root = root
        self.x = x
        self.y = y
        self.enemies = enemies
        self.bullet_label = tk.Label(root, bg="purple", width=2, height=2)
        self.bullet_label.place(x=x, y=y)
        self.speed = 10  # Скорость пули
        self.writ_bar = tk.Label(self.root, bg="#FFF", width=17, height=600)
        self.writ_bar.place(x=1345, y=0)

    def move(self):
        self.x += self.speed
        self.bullet_label.place(x=self.x, y=self.y)
        if self.x < self.root.winfo_width():
            self.root.after(10, self.move)
        else:
            self.bullet_label.destroy()

    def check_collision(self):
        for enemy in self.enemies:
            if abs(self.x - enemy.enemy_button.winfo_x()) < 20 and abs(self.y - enemy.enemy_button.winfo_y()) < 20:
                enemy.destroy_enemy()
                return True
        return False
class Tower:
    def __init__(self, root, x, y, enemies):
        self.root = root
        self.x = x
        self.y = y
        self.enemies = enemies
        self.tower_label = tk.Label(root, bg="white", width=5, height=5)
        self.tower_label.place(x=x, y=y)
        self.bullets_shot = 0
        self.shooting_interval = 2000

    def shoot(self):
        if self.bullets_shot < 10:
            bullet = Bullet(self.root, self.x + 10, self.y + 10, self.enemies)
            bullet.move()
            self.bullets_shot += 1
            if self.bullets_shot < 10:
                self.root.after(self.shooting_interval, self.shoot)
            else:
                self.tower_label.after(self.shooting_interval, self.tower_label.destroy)
        else:
            return

            tower = Tower(root, 100, 100, enemies)
            tower.shoot()

root = tk.Tk()
music_player = Music()
window = Window(root, music_player)
root.mainloop()