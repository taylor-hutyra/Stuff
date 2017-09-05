from tkinter import *
import random



ROWS = 10
COLUMNS = 10
COLOR = ["grey"]*ROWS*COLUMNS
for i,x in enumerate(COLOR):
    if 0.75 < random.random():
        COLOR[i] = "purple"


def button_click(i,j):
    if self.cget('bg') is "grey":
        self.button.configure(bg="purple")
    else:
        self.button.configure(bg="grey")
#Create & Configure root
root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

#Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(ROWS):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(COLUMNS):
        Grid.columnconfigure(frame, col_index, weight=1)
        btn = Button(frame, bg = COLOR[row_index*COLUMNS+col_index], command = button_click) #create a button inside frame
        btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)

root.mainloop()
