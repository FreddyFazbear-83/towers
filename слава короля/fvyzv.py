#import tkinter as tk

#  What happens when the button gets clicked
#def on_button_click(event):
 #   label.config(text=f"что вершит судьбу человества в этом мире?")

#  Create the main app window
#root = tk.Tk()
#root.title("Tkinter Button Event Binding Example")

#  Show the result in a label
#label = tk.Label(root, text="", font=('Arial', 20, 'bold'))
#label.pack(pady=10)

#  Create a button
#button = tk.Button(root, text="Click me!", font=('Arial', 20, 'bold'))

#  Bind the left mouse button click event to the function
#button.bind("<Button-1>", on_button_click)
#button.pack()

#  Let the Tkinter event party begin!
#root.mainloop()

#button.pack(fill=tk.Y, side=tk.LEFT)


from PyQt5 import QtWidgets, QtGui, QtCore
from mydesign import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setFont(
            QtGui.QFont('SansSerif', 30))

        self.ui.label.setGeometry(QtCore.QRect(10, 10, 200, 200))  # изменить геометрию ярлыка


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())