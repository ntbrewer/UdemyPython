#!/bin/python3

from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import numpy as np
plt.clf()
t = plt.figtext(.02,.85,'',fontsize=40)
t.set_text(0.0)

class CalculatorButtons:
    
    def plus(self,event):
        text = float(t.get_text()) + 1
        t.set_text(text)

    def minus(self,event):
        text = float(t.get_text()) - 1
        t.set_text(text)

    def mult(self,event):
        text = float(t.get_text()) * 2
        t.set_text(text)

    def div(self,event):
        text = float(t.get_text()) /2
        t.set_text(text)

callback = CalculatorButtons()
axplus = plt.axes([0.02, 0.05, 0.1, 0.1])
axminus = plt.axes([0.15, 0.05, 0.1, 0.1])
axmult = plt.axes([0.27, 0.05, 0.1, 0.1])
axdiv = plt.axes([0.40, 0.05, 0.1, 0.1])
bplus = Button(axplus, '+')
bplus.on_clicked(callback.plus)
bminus = Button(axminus, '-')
bminus.on_clicked(callback.minus)
bmult = Button(axmult, '*')
bmult.on_clicked(callback.mult)
bdiv = Button(axdiv, '/')
bdiv.on_clicked(callback.div)

plt.show()
