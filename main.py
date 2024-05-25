import tkinter as tk
from PIL import Image, ImageTk
#для кнопки "выход"
from tkinter import messagebox
#для фото с ссылкой
import webbrowser
#для обучения и игры
import random
#для видео
import cv2
#для аудио



root = tk.Tk()
root.title("Glary to the king")
root.geometry("800x600")
root.resizable(False, False)
root.iconbitmap("pichiii/king.ico")

# Задаем фоновое изображение
background_img = ImageTk.PhotoImage(Image.open("pichiii/zam01.jpg"))
background_label = tk.Label(root, image=background_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#кнопка правил игры
#____________________________________________________________________________________________________________________
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Правила игры")
    new_window.iconbitmap("pichiii/king.ico")
    new_window.geometry("800x650")
    new_window.resizable(False, False)
    new_window.configure(bg='gray10')

    # Добавляем информации
    text = tk.Text(new_window, wrap="none", font=("Courier New", 13))
    text.insert("1.0", """ 
        Приветсвую тебя, Игрок, нам очень приятно иметь с вами дело. Надеемся 
    на продолжительную игру с Вами дальше. Ознакомтесь с правилами нашей игры.

        Целью игры является защита собственной базы. Для тебя игрок, есть 
    возможность размещать свои башни, которые способствуют обороне против врагов. 
    Существует только одна локация с существующим маршрутом прохода ботов. 
    Атакующая сторона начинает идти слева направо по определённо отложенному пути. 
    Боты доходят до конца маршрута и наносят урон базы игрока. 

        Для твоей победы необходимо не допускать монстров-ботов до 
    досягаемого урона полем. Именно в избежание этого ставятся оборонительные 
    башни, которые дают сопротивление атакующей части и защиту. 

        Чтобы начать игру необходимо нажать на кнопку «новая игра». 
    После игры внизу есть иконки, которые образуют собой панель управления, где 
    можно начать заново, выйти из игры или поставить на паузу.

        Подробнее:
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        нянянянянянянянянянянянянянянянянянянянянянянянянянянянянхуйяняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        няняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняняня
        """ )
    text.tag_config("red", foreground="red")
    text.tag_config("gray_background", background="gray9")

    text.tag_add("red", "1.0", "end")
    text.tag_add("gray_background", "1.0", "end")

    # Добавляем полосы прокрутки
    scrollbar = tk.Scrollbar(new_window, command=text.yview)
    scrollbar.pack(side="right", fill="y")
    text['yscrollcommand'] = scrollbar.set

    text.pack(fill="both", expand=True)

btn_training = tk.Button(root, text="Правила игры", font=("Courier New", 15), bg="black", fg="red",command=open_new_window)
btn_training.place(x=10, y=500)

#___________________________________________________________________________________________________________________-
#кнопка "выхода"
def exit_app():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

btn_exit = tk.Button(root, text="выход", font=("Courier New", 15), bg="black", fg="red",command=exit_app)
btn_exit.place(x=10, y=550)

def show_hover_message(event):
    messagebox.showinfo("Сплывающее сообщение", "Вы навели курсор на кнопку")

#__________________________________________________________________________________________________________________

#ССЫЛКИ НА СОЦСЕТИ
def open_telegram():
    webbrowser.open('https://web.telegram.org/a/#1778192224')

def open_vk():
    webbrowser.open('https://vk.com/betonoomeshalka')


def open_tgk():
    webbrowser.open('https://t.me/+GLomJd_lv8wzMmVi')

def open_git():
    webbrowser.open('https://github.com/FreddyFazbear-83')

telegram_icon = tk.PhotoImage(file='pichiii/telegram.png')
small_telegram_icon = telegram_icon.subsample(10, 10)  # уменьшение размера в два раза
telegram_button = tk.Button(root, image=small_telegram_icon, command=open_telegram)
telegram_button.pack(side='right', anchor='se', padx=0, pady=0)  # установка в правый нижний угол

vk_icon = tk.PhotoImage(file='pichiii/vk.png')
small_vk_icon = vk_icon.subsample(10, 10)  # уменьшение размера в два раза
vk_button = tk.Button(root, image=small_vk_icon, command=open_vk)
vk_button.pack(side='right', anchor='se', padx=0, pady=0)  # установка в правый нижний угол
vk_button.bind("<Enter>", show_hover_message)


tgk_icon = tk.PhotoImage(file='pichiii/group.png')
small_tgk_icon = tgk_icon.subsample(10, 10)  # уменьшение размера в два раза
tgk_button = tk.Button(root, image=small_tgk_icon, command=open_tgk)
tgk_button.pack(side='right', anchor='se', padx=0, pady=0)  # установка в правый нижний угол

git_icon = tk.PhotoImage(file='pichiii/github.png')
small_git_icon = git_icon.subsample(10, 10)  # уменьшение размера в два раза
git_button = tk.Button(root, image=small_git_icon,  command=open_git)
git_button.pack(side='right', anchor='se', padx=0, pady=0)

#_____________________________________________________________________________________________________________________
#кнопка игры
class VideoPlayer:
    def __init__(self, window, video_source=0, video_file=None, audio_file=None):
        self.window = window

        self.video_source = video_source
        self.video_file = video_file

        if self.video_file is not None:
            self.vid = cv2.VideoCapture(self.video_file)
        else:
            self.vid = cv2.VideoCapture(self.video_source)

        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Добавляем кнопки управления
        self.btn_forward = tk.Button(self.window, text="          Пропустить          ", font=("Courier New", 15), bg="black", fg="red", command=self.skip_forward)
        self.btn_forward.place(x=1065, y=25)

        self.update()

    def update(self):
        ret, frame = self.vid.read()

        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        else:
            # Если достигнут конец видео, оставляем экран пустым
            self.canvas.delete("all")
            # После завершения видео добавляем кнопку выхода
            if not hasattr(self, 'btn_exit'):
                self.btn_exit = tk.Button(self.window, text="Вернуться в главное меню", font=("Courier New", 15), bg="black", fg="red", command=self.window.destroy)
                self.btn_exit.place(x=870, y=190)


        self.window.after(15, self.update)

    def start_audio(self):
        pass  # пустая функция, поскольку аудио отключено

    def stop_audio(self):
        pass  # пустая функция, поскольку аудио отключено

    def skip_forward(self):
        # Остановка аудио (пустая функция, поскольку аудио отключено)
        self.stop_audio()
        # Пропуск вперёд на 5 секунд
        self.vid.set(cv2.CAP_PROP_POS_FRAMES,
                     self.vid.get(cv2.CAP_PROP_POS_FRAMES) + self.vid.get(cv2.CAP_PROP_FPS) * 70)
        # "Пропустить"
        self.btn_forward.destroy()

def win():
    # Создаем новое окно для видеоплеера
    win = tk.Toplevel(root)
    win.title("GttK")
    #win.geometry("1500x850")
    win.attributes('-fullscreen', True)
    win.resizable(False, False)
    win.iconbitmap("pichiii/king.ico")

    # Создаем экземпляр видеоплеера и запускаем его
    player = VideoPlayer(win, video_file="music&video/Gttk2.mp4")
    # player.start_audio()

btn_game = tk.Button(root, text="Начать игру", font=("Courier New", 15), bg="black", fg="red", command=win)
btn_game.place(x=10, y=400)


#______________________________________________________________________________________________________________________
def window():
    def remove_enemy(player):
        global health
        x1, y1, x2, y2 = canvas.coords(player)
        for enemy in enemies:
            ex1, ey1, ex2, ey2 = canvas.coords(enemy)
            if x1 <= ex2 + 10 and x2 >= ex1 - 10 and y1 <= ey2 + 10 and y2 >= ey1 - 10:
                canvas.delete(enemy)
                enemies.remove(enemy)
                health -= 10
                health_label.config(text=f"ХП: {health}")
                if health <= 0:
                    end_game()

    def end_game():
        health_label.config(text="Игра закончена, вы проиграли")
        for button in buttons:
            button.place_forget()
        restart_button = tk.Button(window, text="Хотите повторить?", font=("Helvetica", 16), command=restart_game)
        restart_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def restart_game():
        canvas.delete("all")
        global health
        health = 100
        health_label.config(text="ХП: 100")
        start_game()

    window = tk.Toplevel(root)
    window.title("Обучение")
    window.iconbitmap("pichiii/king.ico")
    window.geometry("800x650")
    window.resizable(False, False)

    canvas = tk.Canvas(window, width=800, height=600, bg="black")
    canvas.pack()

    background_image = ImageTk.PhotoImage(Image.open("pichiii/root.png"))
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    health_label = tk.Label(window, text="ХП: 100", font=("Helvetica", 16), bg="white")
    health_label.place(x=10, y=10)

    players = []
    buttons = []
    enemies = []

    for i in range(3):
        player = canvas.create_rectangle(50, 100*i + 100, 100, 100*i + 150, fill="green")
        players.append(player)
        button = tk.Button(window, text="Удалить врага", font=("Helvetica", 12), command=lambda p=player: remove_enemy(p))
        button.place(x=150, y=100*i + 125)
        buttons.append(button)

    def move_enemies():
        for enemy in enemies:
            canvas.move(enemy, -3, 0)
            ex1, ey1, ex2, ey2 = canvas.coords(enemy)
            for player in players:
                px1, py1, px2, py2 = canvas.coords(player)
                if px1 <= ex2 and px2 >= ex1 and py1 <= ey2 and py2 >= ey1:
                    health -= 1
                    health_label.config(text=f"ХП: {health}")
                    if health <= 0:
                        end_game()

            if ex1 <= 0:
                canvas.move(enemy, 800, 0)

        window.after(30, move_enemies)

    def spawn_enemy():
        enemy = canvas.create_rectangle(800, random.randint(50, 550), 850, random.randint(100, 500), fill="purple")
        enemies.append(enemy)
        window.after(2000, spawn_enemy)

    spawn_enemy()
    move_enemies()

btn_education = tk.Button(root, text="Обучение", font=("Courier New", 15), bg="black", fg="red",command=window)
btn_education.place(x=10, y=448)

root.mainloop()