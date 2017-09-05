from tkinter import *

NUM_STUDENTS = 95
ROWS = 10
COLUMNS = 10
TEXT = ord('A')
SESSION = 2

#Create & Configure root which acts like a window
root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame inside the window
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

#Create a 5x10 (rows x columns) grid of buttons inside the frame
for row_index in range(ROWS):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(COLUMNS):
        Grid.columnconfigure(frame, col_index, weight=1)
        if row_index*COLUMNS + col_index < NUM_STUDENTS:
            Text = chr(TEXT+row_index)+str(SESSION)+str(col_index).zfill(2) + '\n' + 'Name ' + 'SchoolCode' + '\n' + 'Department'
            btn = Button(frame, text=Text, font = ('Arial' , 16)) #create a button inside frame 
            btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)  
root.mainloop()