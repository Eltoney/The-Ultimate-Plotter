from validator import request_graph
from PySide2.QtWidgets import (
    QMainWindow, QApplication, QWidget, QGridLayout, QPushButton,
    QLineEdit, QLabel, QMessageBox, QVBoxLayout)
from PySide2.QtCore import Qt, QSize
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import numpy as np
from plotting import plot_prepare


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


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(1, 1, 1)
        self.setup_grid()
        super(MplCanvas, self).__init__(fig)

    def setup_grid(self):
        self.axes.spines['top'].set_color('none')
        self.axes.spines['right'].set_color('none')
        self.axes.spines['left'].set_linewidth(3)
        self.axes.spines['bottom'].set_linewidth(3)
        self.axes.set_xlabel('X', fontsize=9)
        self.axes.set_ylabel('F(X)', fontsize=9)
        self.axes.tick_params(axis='x', labelsize=9)
        self.axes.tick_params(axis='y', labelsize=9)
        self.axes.xaxis.set_ticks_position('bottom')
        self.axes.yaxis.set_ticks_position('left')
        self.axes.grid(True)

    def plot_graph(self, x, y, func):
        self.axes.set_ylabel(f'F(x) = {func}')
        self.axes.set_title(f'Graph of {func}', color='red')
        self.axes.plot(x, y, '-r')
        self.draw()


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
        self.setFixedSize(QSize(850, 400))

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
        self.graph = MplCanvas()

        layout.addWidget(self.intro, 0, 0, 1, 4)
        layout.addWidget(self.func_label, 2, 0, 1, 1)
        layout.addWidget(self.func_input, 2, 1)
        layout.addWidget(self.min_label, 4, 0, 1, 1)
        layout.addWidget(self.min_input, 4, 1)
        layout.addWidget(self.max_label, 5, 0, 1, 1)
        layout.addWidget(self.max_input, 5, 1)
        layout.addWidget(self.button, 6, 1, 1, 2)
        layout.addWidget(self.graph, 0, 4, 7, 7)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def clear_graph_area(self):
        self.graph.axes.clear()
        self.graph.setup_grid()
        self.graph.draw()

    def process_graph(self):
        min_x = self.min_input.text()
        max_x = self.max_input.text()
        func = self.func_input.text()
        try:
            min_x = float(min_x)
            max_x = float(max_x)
            errors = request_graph(min_x, max_x, func)
            if len(errors) != 0:
                self.clear_graph_area()
                self.dlg = QMessageBox(self)
                self.dlg.setWindowTitle("Error Occurred!")
                msg = 'The following errors occurred: \n'
                if len(errors) == 1:
                    msg = msg[:19] + msg[20:]
                for err in errors:
                    msg += '\t'
                    msg += err
                    msg += '\n'
                self.dlg.setText(msg)
                self.dlg.exec_()
            else:
                self.clear_graph_area()
                paramters = plot_prepare(min_x, max_x, func)
                x = paramters[0]
                y = paramters[1]
                self.graph.plot_graph(x, y, func)
        except:
            self.dlg = QMessageBox(self)
            self.dlg.setWindowTitle("Error Occurred!")
            self.dlg.setText("Please follow the instructions for input")
            self.dlg.exec_()


if __name__ == '__main__':
    app = QApplication()
    w = MainWindow()
    w.show()
    app.exec_()
