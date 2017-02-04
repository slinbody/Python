#!/usr/bin/env python
'''
HD44780 on Raspberry 
'''
#-*-coding:utf8-*-
import RPi.GPIO as GPIO
from time import sleep

RS = 38
RW = 40
EN = 29
D4 = 31
D5 = 33
D6 = 35
D7 = 37
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(EN,  GPIO.OUT)
    GPIO.setup(RS, GPIO.OUT)
    GPIO.setup(RW, GPIO.OUT)
    GPIO.setup(D4, GPIO.OUT)
    GPIO.setup(D5, GPIO.OUT)
    GPIO.setup(D6, GPIO.OUT)
    GPIO.setup(D7, GPIO.OUT)
    GPIO.output(D4,0)
    GPIO.output(D5,0)
    GPIO.output(D6,0)
    GPIO.output(D7,0)
    GPIO.output(RS,0)
    GPIO.output(RW,0)
    GPIO.output(EN,0)

    sleep(0.1)
    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.002)

    GPIO.output(D5,1)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.005)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.0002)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.0002)

    write_command(0x28)
    sleep(0.0001)
    write_command(0x0c)
    sleep(0.0001)
    write_command(0x01)
    sleep(0.002)

def write_command(cmd):
    GPIO.output(EN,0)
    GPIO.output(RW,0)
    GPIO.output(RS,0)
    GPIO.output(D7, 1 if (0x80 & cmd) else 0)
    GPIO.output(D6, 1 if (0x40 & cmd) else 0)
    GPIO.output(D5, 1 if (0x20 & cmd) else 0)
    GPIO.output(D4, 1 if (0x10 & cmd) else 0)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.000001)

    GPIO.output(D7, 1 if (0x08 & cmd) else 0)
    GPIO.output(D6, 1 if (0x04 & cmd) else 0)
    GPIO.output(D5, 1 if (0x02 & cmd) else 0)
    GPIO.output(D4, 1 if (0x01 & cmd) else 0)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.00005)

def write_data(data):
    GPIO.output(EN,0)
    GPIO.output(RW,0)
    GPIO.output(RS,1)  
    GPIO.output(D7, 1 if (0x80 & data) else 0)
    GPIO.output(D6, 1 if (0x40 & data) else 0)
    GPIO.output(D5, 1 if (0x20 & data) else 0)
    GPIO.output(D4, 1 if (0x10 & data) else 0)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.000001)

    GPIO.output(D7, 1 if (0x08 & data) else 0)
    GPIO.output(D6, 1 if (0x04 & data) else 0)
    GPIO.output(D5, 1 if (0x02 & data) else 0)
    GPIO.output(D4, 1 if (0x01 & data) else 0)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.00005)
    
    
def clear():
    write_command(0x01)
    sleep(0.2)

if __name__=="__main__":
    init()
    write_command(0x80)
    write_data(ord("H"))
    write_data(ord("e"))
    write_data(ord("l"))
    write_data(ord("l"))
    write_data(ord("o"))
#    write_data(ord("!"))

    i=0
    while i<9:
        i=i+1
        clear()
        write_command(LCD_LINE_2)
        write_data(ord("i"))
        write_data(ord(":"))
        write_data(ord(str(i)))
        sleep(1)

