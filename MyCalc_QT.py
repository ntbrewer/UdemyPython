
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

class Page(QWidget):

    def __init__(self, parent=None):
        super(Page,self).__init__(parent)

        global total
        lab_layout = QVBoxLayout()
        lab_layout.addWidget(total)
        button_layout_l = QVBoxLayout()
        button_layout_r = QVBoxLayout()
        button_layout_b = QVBoxLayout()
        button_layout_z = QVBoxLayout()
        button_layout_pad_l = QVBoxLayout()
        button_layout_pad_c = QVBoxLayout()
        button_layout_pad_r = QVBoxLayout()

        button_layout_pad_l.addWidget(CalcButtons("7",CalcButtons.clear).button)
        button_layout_pad_l.addWidget(CalcButtons("4",CalcButtons.clear).button)
        button_layout_pad_l.addWidget(CalcButtons("1",CalcButtons.clear).button)
        button_layout_pad_c.addWidget(CalcButtons("8",CalcButtons.clear).button)
        button_layout_pad_c.addWidget(CalcButtons("5",CalcButtons.clear).button)
        button_layout_pad_c.addWidget(CalcButtons("2",CalcButtons.clear).button)
        button_layout_pad_r.addWidget(CalcButtons("9",CalcButtons.clear).button)
        button_layout_pad_r.addWidget(CalcButtons("6",CalcButtons.clear).button)
        button_layout_pad_r.addWidget(CalcButtons("3",CalcButtons.clear).button)
        button_layout_z.addWidget(CalcButtons("0",CalcButtons.clear).button)

        plus_button = CalcButtons("+",CalcButtons.plus)
        button_layout_l.addWidget(plus_button.button)
        minus_button = CalcButtons("-",CalcButtons.minus)
        button_layout_l.addWidget(minus_button.button)
        mult_button = CalcButtons("*",CalcButtons.mult)
        button_layout_l.addWidget(mult_button.button)
        div_button = CalcButtons("/",CalcButtons.div)
        button_layout_l.addWidget(div_button.button)
        button_layout_b.addWidget(CalcButtons("Clear",CalcButtons.clear).button)
        
        mainLayout = QGridLayout()
        mainLayout.addLayout(lab_layout, 0, 0)

        mainLayout.addLayout(button_layout_pad_l, 1, 0)
        mainLayout.addLayout(button_layout_pad_c, 1, 1)
        mainLayout.addLayout(button_layout_pad_r, 1, 2)

        mainLayout.addLayout(button_layout_l, 1, 3)
#        mainLayout.addLayout(button_layout_r, 2, 1)
        mainLayout.addLayout(button_layout_z, 3, 0)
        mainLayout.addLayout(button_layout_b, 3, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My First Qt Calculator")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    total = QLabel("0")
    new_input = "0"
    window = Page()
    window.show()

    sys.exit(app.exec_())
