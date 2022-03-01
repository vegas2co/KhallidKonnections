from tkinter import *
from tkinter.ttk import * 
import random as r

###################### GUI ######################

root = Tk() # create window
root.title('Khallid Konnections Meal Generator')
root.geometry('600x1000')

canvas1 = Canvas(root, bg='white')
canvas1.pack(fill=BOTH, expand=True)

canvas2 = Canvas(root, bg='black')
canvas2.pack(fill=BOTH, expand=True)

###################### FUNCTIONALITY ######################

proteinList = ['Chicken', 'Ground Turkey', 'Shrimp', 'Salmon']
veggiesList = ['Brocolli', 'Zucchini', 'Spinach', 'Kale']
carbsList = ['Sweet Potatoes', 'Noodles', 'Jasmine Rice', 'Toast']
drink = ['Protein Drink']
breakfastList = ['Eggs & toast', 'Oatmeal']

def dailyMeals():
    global lbl
    breakfast = r.choice(breakfastList) #Randomzie meals
    meats = r.choice(proteinList)
    veggies = r.choice(veggiesList)
    carbs = r.choice(carbsList)

    breakfastSentence = 'For breakfast I will be eatiing {}'.format(breakfast)
    lunchSentence = 'For lunch I will be eatiing a healthy serving of {}, {}, {} with a {}'.format(meats,veggies,carbs,drink[0])

    m = r.choice(proteinList) #Randomzie meals again, or this list will be the same as lunch.
    v = r.choice(veggiesList)
    c = r.choice(carbsList)

    dinnerSentence = 'For dinner I will be eatiing a healthy serving of {} {} {}'.format(m,v,c)

    lbl.config(text='Daily Meals:\n'+breakfastSentence + '\n' + lunchSentence + '\n' + dinnerSentence)

###################### BUTTONS ######################

button1 = Button (root, text='Click Meal Generator', command=dailyMeals)
canvas1.create_window(200, 200, window=button1)

lbl = Label(canvas2)
lbl.pack()
lbl.config(background='red')

root.mainloop()