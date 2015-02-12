#!/usr/bin/python3
"""劃同心正方形"""
import turtle

def draw_square(t,size,x):
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.penup()
    t.setpos(-10-x * 10,-10- x * 10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("X")

alex = turtle.Turtle()
alex.pendown()

for i in range(5):
    draw_square(alex,20+20*i,i)

wn.mainloop()
