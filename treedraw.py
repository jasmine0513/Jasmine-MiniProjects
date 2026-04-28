"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""
import turtle

def draw_tree(t, b_length, l_color, t_color):
	t.color(t_color)

	if b_length <= 30:
		t.color(l_color)
		t.forward(b_length)
		t.backward(b_length)
	else:
		t.forward(b_length)
		t.left(30)
		draw_tree(t, b_length * 0.75, l_color, t_color)
		t.right(60)
		draw_tree(t, b_length * 0.75, l_color, t_color)
		t.left(30)
		t.backward(b_length)

tess = turtle.Turtle()
tess.left(90)
tess.pensize(2)
draw_tree(tess,100,"indigo","black")