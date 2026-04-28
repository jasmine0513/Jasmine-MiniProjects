

"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""

import turtle

def polygon(t, n, length, color):
	t.color(color)
	for _ in range(n):
		t.forward(length)
		t.left(360 / n)

def main():
	tess = turtle.Turtle()
	polygon(tess, 5, 100, "green")
	polygon(tess, 6, 60, "#ff00ff")
	polygon(tess, 7, 70, "#ff0000")
	turtle.done()

if __name__ == '__main__':
	main()
