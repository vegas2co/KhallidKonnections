'''from tkinter import *
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
'''

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, salary, sd):
        self.firstname = fname
        self.lastname = lname
        self.salary = salary
        self.sd = sd

    def asdf(self):
        print(self.sd)

    def update(self,sd):
        self.sd = sd

def bs():
    n = 21
    if n > 20 and n % 2 == 0:
        print('Wierd')
    else:
        print('Not Weird')

#x = Student("Mike", "Olsen", '40000', '234')
#x.printname()
#x.asdf()
#x.update('3245647')
#x.asdf()

bs()