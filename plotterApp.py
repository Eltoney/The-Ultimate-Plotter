import sys
from PySide2.QtWidgets import (
    QMainWindow, QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel)
from PySide2.QtCore import Qt, QSize


class MyLabel(QLabel):
    def __int__(self, text):
        super().__init__
        self.setText = text


class MyButton(QPushButton):
    def __int__(self):
        super().__int__()


class MyInputBox(QLineEdit):
    def __init__(self, placeholdText, w, h):
        super().__init__()
        self.setPlaceholderText(placeholdText)
        self.setFixedSize(QSize(w, h))


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        welcome_text = "     Enter your f(x) and we will plot it for you\
            \n\n\nFollow the following rules:\
            \n   1. Only one variable x\
            \n   2. Use supported operations only (+,-,*,/,^)\
            \n   3. Use only only () brackets\
            \n   4. Format brackets corretly\
            \n   5. sin,cos,tan are supported too."
        self.setWindowTitle("The Ultimate Plotter")
        self.setFixedSize(QSize(350, 400))

        layout = QGridLayout()

        layout.addWidget(MyLabel(welcome_text), 0, 0, 1, 4)
        layout.addWidget(MyLabel('Function: '), 2, 0, 1, 1)
        layout.addWidget(MyInputBox(
            'Enter Your f(x) here', 210, 50), 2, 1)
        layout.addWidget(MyLabel('Min x value: '), 4, 0, 1, 1)
        layout.addWidget(MyInputBox('lowest x', 80, 40), 4, 1)
        layout.addWidget(MyLabel('Max x value: '), 5, 0, 1, 1)
        layout.addWidget(MyInputBox('highest x', 80, 40), 5, 1)
        layout.addWidget(MyButton('Plot my graph'), 6, 2, 1, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
