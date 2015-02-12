#!/usr/bin/python3
""" 畫多邊形 """
import turtle

def draw_poly(t,n,size):
    t.pendown()
    for i in range(n):
        t.forward(size)
        t.left(360/n)
    t.penup()
#    t.setpos(-10-x * 10,-10- x * 10)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("X")

alex = turtle.Turtle()
alex.pendown()

draw_poly(alex,20,50)


wn.mainloop()
