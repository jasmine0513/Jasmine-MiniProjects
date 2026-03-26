"""
Jasmine Carrion
jasmine.carrion73.myhunter.cuny.edu

TODO: implement the following pseudocode inside a main() function:
Create a turtle
Set the turtle's speed to 0
Set the turtle's pen size to 2
Hide the turtle

Create a list with ["red", "cyan", "blue", "orange"] repeated 12 times
Create a list with the numbers 20, 22, 24, ..., 114

Zip the two lists

For each color and distance in the zipped lists:
    Set the turtle's color to the current color
    Move forward by the current distance
    Turn left 120 degrees
    Move forward by the current distance again
    Turn right 65 degrees
"""

import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.hideturtle()
colors = ["red", "cyan", "blue", "orange"] * 12
distances = list(range(20, 116, 2))
zipped_lists = zip(colors, distances)

for color, distance in zipped_lists:
    t.color(color)
    t.forward(distance)
    t.left(120)
    t.forward(distance)
    t.right(65)