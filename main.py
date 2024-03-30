import tkinter as tk
from PIL import Image, ImageTk
#для кнопки "выход"
from tkinter import messagebox
#для фото с ссылкой
import webbrowser


root = tk.Tk()
root.title("Glary to the king")
root.geometry("800x600")
root.resizable(False, False)
root.iconbitmap("pichiii/king.ico")


#задаем фоновое изображение
# Задаем фоновое изображение
background_img = ImageTk.PhotoImage(Image.open("pichiii/zam01.jpg"))
background_label = tk.Label(root, image=background_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#кнопка правил игры
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

#копка обучения
def window():
    window = tk.Toplevel(root)
    window.title("Обцчение")
    window.iconbitmap("pichiii/king.ico")
    window.geometry("800x650")
    window.resizable(False, False)


btn_education = tk.Button(root, text="Обучение", font=("Courier New", 15), bg="black", fg="red",command=window)
btn_education.place(x=10, y=448)

#кнопка "выхода"
def exit_app():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

btn_exit = tk.Button(root, text="выход", font=("Courier New", 15), bg="black", fg="red",command=exit_app)
btn_exit.place(x=10, y=550)




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


tgk_icon = tk.PhotoImage(file='pichiii/group.png')
small_tgk_icon = tgk_icon.subsample(10, 10)  # уменьшение размера в два раза
tgk_button = tk.Button(root, image=small_tgk_icon, command=open_tgk)
tgk_button.pack(side='right', anchor='se', padx=0, pady=0)  # установка в правый нижний угол


git_icon = tk.PhotoImage(file='pichiii/github.png')
small_git_icon = git_icon.subsample(10, 10)  # уменьшение размера в два раза
git_button = tk.Button(root, image=small_git_icon,  command=open_git)
git_button.pack(side='right', anchor='se', padx=0, pady=0)

#кнопка игры
def win():
    win = tk.Toplevel(root)
    win.title("начало игры")
    win.iconbitmap("pichiii/king.ico")
    win.geometry("800x650")
    win.resizable(False, False)



btn_game = tk.Button(root, text="Начать игру", font=("Courier New", 15), bg="black", fg="red",command=win)
btn_game.place(x=10, y=396)

root.mainloop()