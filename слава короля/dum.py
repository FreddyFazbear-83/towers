from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(735, 623)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 741, 721))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../towerrr.png"))
        self.label.setObjectName("label")
        self.tk = QtWidgets.QPushButton(self.centralwidget)
        self.tk.setGeometry(QtCore.QRect(10, 380, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.tk.setFont(font)
        self.tk.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.tk.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(170, 0, 0);")
        self.tk.setObjectName("tk")
        self.tk_2 = QtWidgets.QPushButton(self.centralwidget)
        self.tk_2.setGeometry(QtCore.QRect(10, 440, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.tk_2.setFont(font)
        self.tk_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tk_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(170, 0, 0);")
        self.tk_2.setObjectName("tk_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(44)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 251, 121))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(44)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.tk_3 = QtWidgets.QPushButton(self.centralwidget)
        self.tk_3.setGeometry(QtCore.QRect(10, 320, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.tk_3.setFont(font)
        self.tk_3.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.tk_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(170, 0, 0);")
        self.tk_3.setObjectName("tk_3")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 26))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Glory to the king"))
        self.tk.setText(_translate("main", "rules of the game"))
        self.tk_2.setText(_translate("main", "exit"))
        self.label_2.setText(_translate("main", " Glory to the king "))
        self.label_3.setText(_translate("main", " ___    ________________    "))
        self.tk_3.setText(_translate("main", "start the games"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())

import pygame
import sys

# Инициализация pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Передвижение предмета по клику мыши")

# Загрузка изображения
image = pygame.image.load('nefrit.ico')
image_rect = image.get_rect()

# Установка начальной позиции предмета
image_rect.center = (200, 150)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            image_rect.center = event.pos

    # Отрисовка
    screen.fill(WHITE)
    screen.blit(image, image_rect)
    
    pygame.display.flip()

# Завершение работы pygame
pygame.quit()
sys.exit()
