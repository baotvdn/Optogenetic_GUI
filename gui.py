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
#root.config(background = "#FFFFFF")


leftFrame = Frame(root, width=600, height = 200)
leftFrame.grid(row=0, column=0, padx=10, pady=2)
#Label(leftFrame, text="Waveform").grid()

#Channel
channel = Text(leftFrame, width = 30, height = 10)
channel.grid(row=0, column=0, padx=10, pady=2)
Label(channel, text = "Channel", font="Helvetica 16 bold").grid(row=0, column=2, columnspan=3)


def checkbar():
	var_c = []
#	mat = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],
#	[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],
#	[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7]]
	mat = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24]
	i = 1 
	j = 0
	for pick in mat:
		var = IntVar()
		chk = Checkbutton(channel, text=pick, variable=var)
		chk.grid(row=i, column=j)
		var_c.append(var)
		j = j + 1
		if j == 7:
			i = i + 1
			j = 0
	return 

chn = checkbar()


#Frequency
frequency = Frame(leftFrame, width=200, height = 200)
frequency.grid(row=1, column=0, padx=10, pady=2)

def sel():
#   selection = "You selected the option " + str(var.get())
#   label.config(text = selection)
	pass

var = IntVar()

Label(frequency, text = "Frequency", font="Helvetica 16 bold").grid(row=0, column=0)

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
btnFrame.grid(row=2, column=0, padx=10, pady=2)
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


signal = Frame(rightFrame, width=200, height = 200)
signal.grid(row=0, column=0, columnspan=3, padx=10, pady=2)

#wave = Menubutton(top, text="wave", relief=RAISED)
#wave.grid(row=0, column=0)
tkvar = StringVar()
choices = { 'Random','Sin','Step','Ram'}
tkvar.set('Random') # set the default option
 
wave = OptionMenu(signal, tkvar, *choices)
Label(signal, text="Wave").grid(row = 0, column = 0)
wave.grid(row = 0, column =1)
 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
 
# link function to change dropdown
#tkvar.trace('a', change_dropdown)

tkvar1 = StringVar()
choices1 = { 'Pattern1','Pattern2','Pattern3','Pattern4'}
tkvar1.set('Pattern1') # set the default option
 
pattern = OptionMenu(signal, tkvar1, *choices1)
Label(signal, text="Pattern").grid(row = 1, column = 0)
pattern.grid(row = 1, column =1)

Label(signal, text="Enter time in seconds").grid(row = 2, column =0)
E1 = Entry(signal, bd =5)
E1.grid(row = 2, column =1)


circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
circleCanvas.grid(row=1, column=0, columnspan=3, padx=10, pady=2)

button = Frame(rightFrame, width=200, height = 200)
button.grid(row=3, column=0, padx=10, pady=2)

run_button = Button(button, text="Run", command=led_off, height=2, width=8)
run_button.grid(row=0, column=0)

off_button = Button(button, text="Turn Off", command=led_off, height=2, width=8)
off_button.grid(row=0, column=3)

exitButton = Button(button, text="Exit", command=exitProgram, height=2, width=8)
exitButton.grid(row=0, column=6)

'''
exitButton = Button(win, text="Exit", command=exitProgram, height=2, width=6)
exitButton.pack(side=BOTTOM)

off_button = Button(win, text="Off", command=led_off, height=2, width=8)
off_button.pack()
'''
mainloop()
