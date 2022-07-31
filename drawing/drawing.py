#!/usr/bin/env python3
import turtle

pen = turtle.Turtle()

pen.shape("turtle")
# pen.hideturtle()
b = (0.0, 0.0, 1.0)
pen.fillcolor(b)
pen.begin_fill()
pen.right(90)
pen.forward(100)
pen.right(90)
pen.fd(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.circle(80)
pen.end_fill()
for i in range(5):
    pen.pendown()
    pen.fd(200)
    pen.right(144)


pen.home()

turtle.done()
