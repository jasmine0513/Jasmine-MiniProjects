
"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(5):
    color = input("Enter color (as hex): ")
    t.fillcolor(color)
    t.begin_fill()
    t.forward(20)
    t.end_fill()
    t.stamp()
    t.forward(20)


