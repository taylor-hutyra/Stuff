from tkinter import *

color="purple"
default_color="white"
ROWS = 10
COLUMNS = 10
button_list = [default_color]*(ROWS*COLUMNS)

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
            b = Button(frame, bg=default_color, activebackground=default_color)
            b.grid(column=y, row=x)
            # creating the callback with "b" as the default parameter bellow "freezes" its value pointing
            # to the button created in each run of the loop.
            b["command"] = lambda b=b, x=x, y=y: click(b, x, y)
            b.grid(row=x, column=y, sticky=N+S+E+W)
    return window

def click(button,x,y):
    if button_list[x*ROWS+y] is color:
        button_list[x*ROWS+y] = default_color
        button["bg"] = default_color
        button["activebackground"] = default_color
    else:
        button_list[x*ROWS+y] = color
        button["bg"] = color
        button["activebackground"] = color
w = main()
mainloop()
