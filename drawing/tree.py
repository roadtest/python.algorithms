#!/usr/bin/env python3
import turtle

t = turtle.Turtle()
w = turtle.Screen()
t.speed(0)
t.color("brown")


def left_curve(length, angle):
    t.setheading(0)  # Head to the right
    t.right(angle)
    i = 0
    while i < length:
        t.forward(2)
        t.right(1)
        i += 1


def left_curve_1(length, angle):
    t.setheading(0)  # Head to the right
    t.right(angle)
    i = 0
    while i < length:
        t.forward(2)
        t.left(1)
        i += 1


def left_spike(length, angle):
    t.setheading(0)  # Head to the right
    t.left(angle)
    i = 0
    while i < length:
        t.forward(2)
        t.left(1)
        i += 1


def straight_line_down(length, angle):
    t.setheading(0)
    t.right(angle)
    t.forward(length)


def draw_tree():
    t.penup()
    # start point for tree
    t.goto(-250, 300)
    t.color("brown")
    # start draw left side of tree
    t.pendown()
    left_curve(40, 91)
    left_spike(15, 92)
    left_curve(40, 90)
    left_curve_1(40, 100)
    left_spike(15, 120)
    left_curve(20, 90)
    left_curve_1(20, 100)
    left_spike(15, 160)
    left_curve(20, 30)
    straight_line_down(5, 40)
    straight_line_down(5, 60)
    straight_line_down(20, 90)
    left_curve_1(80, 120)
    t.penup()

    # start point for tree
    t.goto(-250, 300)
    t.color("brown")
    t.pendown()
    # start draw right side of tree
    left_curve(60, 45)
    left_spike(15, 45)
    left_curve(60, 45)
    t.circle(10, 180)
    left_curve(60, 45)
    left_spike(15, 45)
    left_curve(80, 45)
    t.penup()

    # add some tree branches
    t.goto(-250, 220)
    t.pendown()
    straight_line_down(40, 90)
    t.penup()
    t.goto(-260, 160)
    t.pendown()
    straight_line_down(40, 90)
    t.penup()
    t.goto(-255, 100)
    t.pendown()
    left_curve_1(40, 95)
    t.penup()
    t.goto(-260, 0)
    t.pendown()
    straight_line_down(20, 60)
    t.penup()
    t.goto(-110, -10)
    t.pendown()
    straight_line_down(20, 110)
    t.penup()
    t.goto(-110, -60)
    t.pendown()
    straight_line_down(20, 85)
    t.penup()
    t.goto(-260, -60)
    t.pendown()
    straight_line_down(20, 120)

    print(t.pos())

    # w.exitonclick()
