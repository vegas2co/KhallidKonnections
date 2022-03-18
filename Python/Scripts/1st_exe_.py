from tkinter import *
from tkinter.ttk import * 
import random as r

###################### GUI ######################

root = Tk() # create window
root.title('Khallid Konnections Meal Generator')
root.geometry('600x1000')

canvas1 = Canvas(root, bg='white')
canvas1.pack(fill=BOTH, expand=True)

button1 = Button (root, text='Click Meal Generator')


###################### FUNCTIONALITY ######################






###################### BUTTONS ######################

#button1 = Button (root, text='Click Meal Generator', command=dailyMeals)
canvas1.create_window(200, 200, window=button1)


root.mainloop()