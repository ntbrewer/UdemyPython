#!/bin/python3
# Calc from python-complete by Joseph Delgadillo
import re

print("Our Magical Calculator")
print("Type 'q' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter expression:")
    else: 
        equation = input(str(previous))

    if equation == 'q':
        print("Goodbye.")
        run = False

    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '',equation) 
        #guards against injection but also prevents trig functions, etc
        
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
