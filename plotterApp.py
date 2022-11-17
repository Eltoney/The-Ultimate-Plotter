import sys
from validator import request_graph
from PySide2.QtWidgets import (
    QMainWindow, QApplication, QWidget, QGridLayout, QPushButton,
    QLineEdit, QLabel, QMessageBox)
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
            \n   5. sin,cos,tan are supported too.\
            \n   6. min and max value of x has to real numbers\
            \n      e.g: sin(x) + 5 * x + 3^2  + 10"
        self.setWindowTitle("The Ultimate Plotter")
        self.setFixedSize(QSize(350, 400))

        layout = QGridLayout()

        self.intro = MyLabel(welcome_text)
        self.func_label = MyLabel('Function: ')
        self.func_input = MyInputBox('Enter Your f(x) here', 210, 50)
        self.min_label = MyLabel('Min x value: ')
        self.min_input = MyInputBox('lowest x', 80, 40)
        self.max_label = MyLabel('Max x value: ')
        self.max_input = MyInputBox('highest x', 80, 40)
        self.button = MyButton('Plot my graph')
        self.button.clicked.connect(self.process_graph)

        layout.addWidget(self.intro, 0, 0, 1, 4)
        layout.addWidget(self.func_label, 2, 0, 1, 1)
        layout.addWidget(self.func_input, 2, 1)
        layout.addWidget(self.min_label, 4, 0, 1, 1)
        layout.addWidget(self.min_input, 4, 1)
        layout.addWidget(self.max_label, 5, 0, 1, 1)
        layout.addWidget(self.max_input, 5, 1)
        layout.addWidget(self.button, 6, 2, 1, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def process_graph(self):
        min_x = self.min_input.text()
        max_x = self.max_input.text()
        func = self.func_input.text()
        graphing_errors = []
        try:
            min_x = float(min_x)
            max_x = float(max_x)
            graphing_errors = request_graph(min_x, max_x, func)
            if graphing_errors != 1:
                self.dlg = QMessageBox(self)
                self.dlg.setWindowTitle("Error Occurred!")
                msg = 'The following errors occurred: \n'
                if len(graphing_errors) == 1:
                    msg = msg[:19] + msg[20:]
                for err in graphing_errors:
                    msg += '\t'
                    msg += err
                    msg += '\n'
                self.dlg.setText(msg)
                self.dlg.exec_()
        except:
            self.dlg = QMessageBox(self)
            self.dlg.setWindowTitle("Error Occurred!")
            self.dlg.setText("Please follow the instructions for input")
            self.dlg.exec_()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
