from tkinter import *
from tkinter.ttk import * 
from tkinter import messagebox
from tkinter import simpledialog
import random as r

###################### GUI ######################

root = Tk() # create window
root.title('Khallid Konnections Meal Generator')
root.geometry('600x800')

canvas1 = Canvas(root, bg='white')
canvas1.pack(fill=BOTH, expand=True)

canvas2 = Canvas(root, bg='black')
canvas2.pack(fill=BOTH, expand=True)

###################### Functionality ######################

proteinList = ['Chicken', 'Ground Turkey', 'Shrimp', 'Salmon']
veggiesList = ['Brocolli', 'Zucchini', 'Spinach', 'Kale']
carbsList = ['Sweet Potatoes', 'Noodles', 'Jasmine Rice', 'Toast']
drink = ['Protein Drink']
breakfastList = ['Eggs & toast', 'Oatmeal']

def dailyMeals():
    breakfast = r.choice(breakfastList)
    meats = r.choice(proteinList)
    veggies = r.choice(veggiesList)
    carbs = r.choice(carbsList)

    breakfastSentence = 'For breakfast I will be eatiing {}'.format(breakfast)
    lunchSentence = 'For lunch I will be eatiing a healthy serving of {}, {}, {} with a {}'.format(meats,veggies,carbs,drink[0])

    m = r.choice(proteinList)
    v = r.choice(veggiesList)
    c = r.choice(carbsList)

    dinnerSentence = 'For dinner I will be eatiing a healthy serving of {} {} {}'.format(m,v,c)

    return breakfastSentence + '\n' + lunchSentence + '\n' + dinnerSentence
    
    '''
    p = meats

    proteinList.remove(p)
    print(breakfastSentence)
    print(lunchSentence)
    print(dinnerSentence + '\n
    '''

###################### BUTTONS ######################

button1 = Button (root, text='Click Meal Generator', command=dailyMeals())
canvas1.create_window(200, 200, window=button1)

Label(canvas2, text=dailyMeals()).pack()

root.mainloop()