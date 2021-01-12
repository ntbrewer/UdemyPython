
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


class CalcButtons:

    def __init__(self, symbol, call):
        self.button = QPushButton(" " + symbol + " ")
        self.button.clicked.connect(call)

    def plus(self):
        global total
        text = float(total.text()) + 1
        total.setText(str(text))

    def minus(self):
        global total
        text = float(total.text()) - 1
        total.setText(str(text))

    def mult(self):
        global total
        text = float(total.text()) * 2
        total.setText(str(text))

    def div(self):
        global total
        text = float(total.text()) / 2
        total.setText(str(text))

    def clear(self):
        global total
        total.setText("0")

    def equals(self):
        global total
        global display
        display.setText(total.text())

    def no(self):
        pass

class PadButtons:

    def __init__(self, symbol, call):
        self.button = QPushButton(" " + symbol + " ")
        self.button.clicked.connect(call)

    def zero(self):
        global new_input
        global display
        if new_input != "0":
            new_input = new_input + "0"
        display.setText(new_input)

    def one(self):
        global new_input
        if new_input != "0":
            new_input = new_input + "1"
        else:
            new_input = "1"
        display.setText(new_input)

    def two(self):
        global new_input
        if new_input != "0":
            new_input = new_input + "2"
        else:
            new_input = "2"
        display.setText(new_input)

    def three(self):
        global new_input
        if new_input != "0":
            new_input = new_input + "3"
        else:
            new_input = "3"
        display.setText(new_input)

    def four(self):
        global new_input
        if new_input != "0":
            new_input = new_input + "4"
        else:
            new_input = "4"
        display.setText(new_input)

    def five(self):
        global new_input
        if new_input != "0":
            new_input = new_input + "5"
        else:
            new_input = "5"
        display.setText(new_input)

    def six(self):
        global new_input
        if new_input != "0":
            new_input = new_input + "6"
        else:
            new_input = "6"
        display.setText(new_input)

    def seven(self):
        global new_input
        if new_input != "0":
            new_input = new_input + "7"
        else:
            new_input = "7"
        display.setText(new_input)

    def eight(self):
        global new_input
        if new_input != "0":
            new_input = new_input + "8"
        else:
            new_input = "8"
        display.setText(new_input)

    def nine(self):
        global new_input
        if new_input != "0":
            new_input = new_input + "9"
        else:
            new_input = "9"
        display.setText(new_input)

class Page(QWidget):

    def __init__(self, parent=None):
        super(Page,self).__init__(parent)

        global display
        lab_layout = QVBoxLayout()
        lab_layout.addWidget(display)
        button_layout_l = QVBoxLayout()
        button_layout_r = QVBoxLayout()
        button_layout_b = QVBoxLayout()
        button_layout_z = QVBoxLayout()
        button_layout_pad_l = QVBoxLayout()
        button_layout_pad_c = QVBoxLayout()
        button_layout_pad_r = QVBoxLayout()

        button_layout_pad_l.addWidget(PadButtons("7",PadButtons.seven).button)
        button_layout_pad_l.addWidget(PadButtons("4",PadButtons.four).button)
        button_layout_pad_l.addWidget(PadButtons("1",PadButtons.one).button)
        button_layout_pad_l.addWidget(PadButtons("0",PadButtons.zero).button)

        button_layout_pad_c.addWidget(PadButtons("8",PadButtons.eight).button)
        button_layout_pad_c.addWidget(PadButtons("5",PadButtons.five).button)
        button_layout_pad_c.addWidget(PadButtons("2",PadButtons.two).button)
        button_layout_pad_c.addWidget(CalcButtons("=",CalcButtons.equals).button)

        button_layout_pad_r.addWidget(PadButtons("9",PadButtons.nine).button)
        button_layout_pad_r.addWidget(PadButtons("6",PadButtons.six).button)
        button_layout_pad_r.addWidget(PadButtons("3",PadButtons.three).button)
        button_layout_pad_r.addWidget(CalcButtons("",CalcButtons.no).button)


        plus_button = CalcButtons("+",CalcButtons.plus)
        button_layout_l.addWidget(plus_button.button)
        minus_button = CalcButtons("-",CalcButtons.minus)
        button_layout_l.addWidget(minus_button.button)
        mult_button = CalcButtons("*",CalcButtons.mult)
        button_layout_l.addWidget(mult_button.button)
        div_button = CalcButtons("/",CalcButtons.div)
        button_layout_l.addWidget(div_button.button)
        button_layout_l.addWidget(CalcButtons("Clear",CalcButtons.clear).button)
        
        mainLayout = QGridLayout()
        mainLayout.addLayout(lab_layout, 0, 0)

        mainLayout.addLayout(button_layout_pad_l, 1, 0)
        mainLayout.addLayout(button_layout_pad_c, 1, 1)
        mainLayout.addLayout(button_layout_pad_r, 1, 2)

        mainLayout.addLayout(button_layout_l, 1, 3)

        self.setLayout(mainLayout)
        self.setWindowTitle("My First Qt Calculator")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    total = QLabel("0")
    new_input = "0"
    display = QLabel("0")
    window = Page()
    window.show()

    sys.exit(app.exec_())
