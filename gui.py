#Senior Design
from tkinter import *

#import RPi.GPIO as GPIO

'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.output(36, GPIO.LOW)
GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.LOW)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)
'''

root = Tk()

def red_on():
#    GPIO.output(36,GPIO.HIGH)
	circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='red')
#    colorLog.insert(0.0, "Red\n")
    
def green_on():
#    GPIO.output(38,GPIO.HIGH)
	circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='green')
#    colorLog.insert(0.0, "Green\n")

def blue_on():
#    GPIO.output(40,GPIO.HIGH)
	circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='blue')
#    colorLog.insert(0.0, "Green\n")
    
def led_off():
#    GPIO.output(36,GPIO.LOW)
#    GPIO.output(38,GPIO.LOW)
#    GPIO.output(40,GPIO.LOW)
	pass

def exitProgram():
#    GPIO.cleanup()
    root.quit()


root.title("Optogenetic Platform")
#root.geometry('800x480')
root.config(background = "#FFFFFF")


leftFrame = Frame(root, width=600, height = 200)
leftFrame.grid(row=0, column=0, padx=10, pady=2)
#Label(leftFrame, text="Waveform").grid()

#Waveform
colorLog = Text(leftFrame, width = 30, height = 10, takefocus=0)
colorLog.grid(row=0, column=0, padx=10, pady=2)

#Frequency
frequency = Frame(leftFrame, width=200, height = 200)
frequency.grid(row=1, column=0, padx=10, pady=2)

def sel():
#   selection = "You selected the option " + str(var.get())
#   label.config(text = selection)
	pass

var = IntVar()

Label(frequency, text = "Frequency").grid(row=0, column=0)

R1 = Radiobutton(frequency, text="0.5 Hz", variable=var, value=1, command=sel)
R1.grid(row=1, column=0)

R2 = Radiobutton(frequency, text="1.0 Hz", variable=var, value=2, command=sel)
R2.grid(row=2, column=0)

R3 = Radiobutton(frequency, text="2.0 Hz", variable=var, value=3, command=sel)
R3.grid(row=3, column=0)

label = Label(frequency)
label.grid(row=4, column=0)
#Instruct = Label(leftFrame, text="test\n")
#Instruct.grid(row=1, column=0, padx=10, pady=2)

'''
try:
    imageEx = PhotoImage(file = 'image.gif')
    Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=2)
except:
    print("Image not found") '''

#Button
var_red = DoubleVar()
var_green = DoubleVar()
var_blue = DoubleVar()

btnFrame = Frame(leftFrame, width=200, height = 200)
btnFrame.grid(row=3, column=0, padx=10, pady=2)
Label(btnFrame, text = "Brightness", font="Helvetica 16 bold").grid(row=1, column=1)

red_led = Button(btnFrame, text="Red", command=red_on, height=2, width=8)
red_led.grid(row=0, column=0, padx=10, pady=2)
red_slider = Scale(btnFrame, variable = var_red, orient=HORIZONTAL)
red_slider.grid(row=2, column=0)

green_led = Button(btnFrame, text="Green", command=green_on, height=2, width=8)
green_led.grid(row=0, column=1, padx=10, pady=2)
green_slider = Scale(btnFrame, variable = var_green, orient=HORIZONTAL)
green_slider.grid(row=2, column=1)

blue_led = Button(btnFrame, text="Blue", command=blue_on, height=2, width=8)
blue_led.grid(row=0, column=2, padx=10, pady=2)
blue_slider = Scale(btnFrame, variable = var_blue, orient=HORIZONTAL)
blue_slider.grid(row=2, column=2)





#Right frame


rightFrame = Frame(root, width=200, height = 600)
rightFrame.grid(row=0, column=1, padx=10, pady=2)


colorLog = Text(rightFrame, width = 30, height = 10, takefocus=0)
colorLog.grid(row=0, column=0, columnspan=3, padx=10, pady=2)

circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
circleCanvas.grid(row=1, column=0, columnspan=3, padx=10, pady=2)

run_button = Button(rightFrame, text="Run", command=led_off, height=2, width=8)
run_button.grid(row=2, column=0)

off_button = Button(rightFrame, text="Turn Off", command=led_off, height=2, width=8)
off_button.grid(row=2, column=1)

exitButton = Button(rightFrame, text="Exit", command=exitProgram, height=2, width=6)
exitButton.grid(row=2, column=2)

'''
exitButton = Button(win, text="Exit", command=exitProgram, height=2, width=6)
exitButton.pack(side=BOTTOM)

off_button = Button(win, text="Off", command=led_off, height=2, width=8)
off_button.pack()
'''
mainloop()