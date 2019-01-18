#Senior Design
from tkinter import *

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.output(36, GPIO.LOW)
GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.LOW)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)


win = Tk()

def red_on():
    GPIO.output(36,GPIO.HIGH)
    
def green_on():
    GPIO.output(38,GPIO.HIGH)

def blue_on():
    GPIO.output(40,GPIO.HIGH)
    
def led_off():
    GPIO.output(36,GPIO.LOW)
    GPIO.output(38,GPIO.LOW)
    GPIO.output(40,GPIO.LOW)

def exitProgram():
    GPIO.cleanup()
    win.quit()


win.title("GUI")
win.geometry('800x480')

exitButton = Button(win, text="Exit", command=exitProgram, height=2, width=6)
exitButton.pack(side=BOTTOM)

red_led = Button(win, text="Red", command=red_on, height=2, width=8)
red_led.pack()

green_led = Button(win, text="Green", command=green_on, height=2, width=8)
green_led.pack()

blue_led = Button(win, text="Blue", command=blue_on, height=2, width=8)
blue_led.pack()

off_button = Button(win, text="Off", command=led_off, height=2, width=8)
off_button.pack()

mainloop()
