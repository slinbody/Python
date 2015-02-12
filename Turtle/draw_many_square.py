#!/usr/bin/python3
""" 畫很多正方形 """
import turtle

def draw_square(t,size):
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.penup()
#    t.setpos(-10-x * 10,-10- x * 10)
#    t.forward(10)
#    t.left(180)

def draw_20(t,size):
    t.pendown()
    draw_square(t,size)
    t.left(18)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("X")

alex = turtle.Turtle()
alex.pendown()
#alex.ht()
#alex.setpos(-10,-10)
#alex.setpos(-20,-20)
#turtle.setup(startx=-300)

for i in range(20):
    #draw_square(alex,20+20*i,i)
    draw_20(alex,100)

wn.mainloop()
