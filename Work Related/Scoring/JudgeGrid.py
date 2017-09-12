from tkinter import *
from random import random

color="purple"
default_color="white"
ROWS = 10
COLUMNS = 10
NUMJUDGES = 2
button_list = []
for i in range(ROWS*COLUMNS):
    button_list.append([default_color, 2])

def main():
    window = Tk()
    Grid.rowconfigure(window, 0, weight=1)
    Grid.columnconfigure(window, 0, weight=1)
    frame=Frame(window)
    frame.grid(row=0, column=0, sticky=N+S+E+W)
    for x in range(ROWS):
        Grid.rowconfigure(frame, x, weight=1)
        for y in range(COLUMNS):
            Grid.columnconfigure(frame, y, weight=1)
            b = Button(frame,text = str(x)+str(y) + '- NEEDS ' + str(NUMJUDGES), bg=default_color, activebackground=default_color)
            b.grid(column=y, row=x)
            b["command"] = lambda b=b, x=x, y=y: click(b, x, y)
            b.grid(row=x, column=y, sticky=N+S+E+W)
    Grid.columnconfigure(frame, COLUMNS, weight=1)
    Grid.rowconfigure(frame, int(ROWS/2), weight=1)
    b = Button(frame, text = 'update', bg = default_color, activebackground = default_color)
    b["command"] = lambda : update()
    b.grid(column = COLUMNS, row = int(ROWS/2), sticky = N+S+E+W)
    return window

def click(button,x,y):
    if button_list[x*ROWS+y][0] is color:
        button_list[x*ROWS+y][0] = default_color
        button_list[x*ROWS+y][1] -= 1
        button["bg"] = default_color
        button["activebackground"] = default_color
        button["text"] = str(x)+str(y)+ '- NEEDS ' + str(button_list[x*ROWS+y][1])
    elif button_list[x*ROWS+y][0] is default_color:
        button_list[x*ROWS+y][0] = color
        button["bg"] = color
        button["activebackground"] = color
        button["text"] = str(x)+str(y) + '- JUDGING'
    if button_list[x*ROWS+y][1] is 0:
        button_list[x*ROWS+y][0] = "grey"
        button["bg"] = "grey"
        button["activebackground"] = "grey"
        button["text"] = str(x)+str(y)+ '- DONE'
    print(button_list)

def update():
    global color
    color = 'red'
w = main()
mainloop()
