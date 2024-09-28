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
import pyaudio
import wave
import threading


class Music:
    def play_music(file_path):
        def play_stream():
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
        thread = threading.Thread(target=play_stream)
        thread.daemon = True
        thread.start()
Music.play_music("C:/Users/Vika/Documents/GitHub/towers/playy/большевики_грибоеды_грустная_повседневка.wav")

root = tk.Tk()
root.title("Стреляющие башни")
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
    new_window.geometry("850x650")
    new_window.resizable(False, False)
    new_window.configure(bg='red')

    # Добавляем информации
    text = tk.Text(new_window, wrap="none", font=("Courier New", 13))
    text.insert("1.0", """ 
        Приветсвую тебя, Игрок, нам очень приятно иметь с вами дело. Надеемся 
    на продолжительную игру с Вами дальше. Ознакомтесь с правилами нашей игры.

        Целью игры является защита собственной базы. Для тебя игрок, есть 
    возможность размещать свои башни, которые способствуют обороне против врагов. 
    Существует только одна локация с существующим маршрутом прохода ботов. 
    Атакующая сторона начинает идти справа налево по определённо отложенному пути. 
    Боты доходят до конца маршрута и наносят урон базы игрока. 

        Для твоей победы необходимо не допускать монстров-ботов до 
    досягаемого урона полем. Именно в избежание этого ставятся оборонительные 
    башни, которые дают сопротивление атакующей части и защиту. 

        Чтобы начать игру необходимо нажать на кнопку «новая игра». 
    После игры внизу есть иконки, которые образуют собой панель управления, где 
    можно начать заново, выйти из игры или поставить на паузу.
    
    
        Подробнее:
        На игровом поле для Вас предвставлены различные кнопочки. 
        - "стрелочка указывающая влево" -- означает что это выход из игры, но если
    Вы находитесь в режиме "Новая игра", тогда происходит полный выход из игры.
        - "круговая стрелочка" -- начинает игру заново.
        - "замок с зелёным плюсом" -- с помощью этой кнопки Вам возможна покупка 
    башни.(их стоимость 500 монет)
    !НО помните, они могут выстрелить лишь 10 раз, после ломаются!
        - "монетки" - начисляются вам за побеждённых врагов.  
        - "знак черепа" - это главный счётчик Ваших побед.
        
        
        Вам будет интересно:
        Эта игра является пробноким будущего проекта. Цельный контент будет 
    доступен после полной реализиции данного продукта. 
        Сюжет лежит мир иной вселеной, где после некого инцидента привычный мир 
    стал другим. Появились некие существа, похожие на зверо-людей, которые были 
    против человечесва. Их целью была лишь злоба и угнетение всего живого.  
    Учавствуя в сражениях и решая загадки, Вы узнаёте тайны этого мира и помогаете 
    спасти свой народ. 
    
      

        
        """ )
    text.tag_config("red", foreground="red")
    text.tag_config("gray_background", background="gray9")

    text.tag_add("red", "1.0", "end")
    text.tag_add("gray_background", "1.0", "end")

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
    messagebox.showinfo("Сплывающее сообщение", "У вас не доступена сеть для перехода в интернет")

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
        self.audio_file = audio_file
        if self.audio_file is not None:
            self.audio_thread = threading.Thread(target=self.play_audio)
            self.audio_thread.daemon = True
            self.audio_thread.start()

        self.btn_forward = tk.Button(self.window, text="          Пропустить          ", font=("Courier New", 15), bg="black", fg="red", command=self.skip_forward)
        self.btn_forward.place(x=1065, y=25)

        self.update()

    def update(self):
        try:
            ret, frame = self.vid.read()

            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            else:
                self.canvas.delete("all")
                if not hasattr(self, 'btn_exit'):
                    self.btn_exit = tk.Button(self.window, text="Вернуться в главное меню",
                                              font=("Courier New", 15), bg="black", fg="red",
                                              command=self.window.destroy)
                    self.btn_exit.place(x=870, y=190)

            self.window.after(15, self.update)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def play_audio(self):
        wf = wave.open(self.audio_file, 'rb')
        p = pyaudio.PyAudio()

        self.stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                             channels=wf.getnchannels(),
                             rate=wf.getframerate(),
                             output=True)
        data = wf.readframes(1024)
        while data != b'' and self.stream.is_active():
            self.stream.write(data)
            data = wf.readframes(1024)

        self.stream.stop_stream()
        self.stream.close()
        p.terminate()

    def stop_audio(self):
        if hasattr(self, 'stream') and self.stream.is_active():
            self.stream.stop_stream()
            self.stream.close()
            p = pyaudio.PyAudio()
            p.terminate()

    def run_file(self):
        try:
            subprocess.Popen(["python", "playy/main.py"])
        except Exception as e:
            print(f"Ошибка при запуске внешнего файла: {e}")

    def skip_forward(self):
        self.stop_audio()
        frame_jump = self.vid.get(cv2.CAP_PROP_FPS) * 5
        self.vid.set(cv2.CAP_PROP_POS_FRAMES,
                     self.vid.get(cv2.CAP_PROP_POS_FRAMES) + frame_jump)
        self.run_file()
        import os
        os._exit(0)


def win():
    win = tk.Toplevel(root)
    win.title("Стреляющие башни")
    win.attributes('-fullscreen', True)
    win.resizable(False, False)
    win.iconbitmap("pichiii/king.ico")

    player = VideoPlayer(win, video_file="music&video/gttk2.mp4", audio_file="music&video/GttK.wav")

btn_game = tk.Button(root, text="Сюжетный видеофрагмент", font=("Courier New", 15), bg="black", fg="red", command=win)
btn_game.place(x=10, y=350)


#______________________________________________________________________________________________________________________
import subprocess
import os
def run_second_file():
    subprocess.run(["python", "playy/main.py"])
    os._exit(0)

btn_education = tk.Button(root, text="Обучение: Волна 1", font=("Courier New", 10), bg="black", fg="red",command=run_second_file)
btn_education.place(x=10, y=400)
#__________________________________________
def run_second_file2():
    subprocess.run(["python", "play2/main.py"])
    os._exit(0)

btn_education = tk.Button(root, text="Обучение: Волна 2", font=("Courier New", 10), bg="black", fg="red",command=run_second_file2)
btn_education.place(x=10, y=448)

root.mainloop()