from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def login():
    pass

def register():
    pass


root=Tk() # create window
canvas1 = Canvas(root, width = 600, height = 600, bg='white')
canvas1.pack()

#Login or Register button
loginButton = Button (root, text='Login',font=("Arial", 12))
canvas1.create_window(260, 25, window=loginButton)

registerButton = Button (root, text='Register',font=("Arial", 12))
canvas1.create_window(340, 25, window=registerButton)

#Greeting
greeting = Label(root, text='Login', font=("Arial", 24))
canvas1.create_window(300, 85, window=greeting)

#userName
username = Label(root, text='UserName', font=("Arial", 12))
canvas1.create_window(250, 140, window=username)

user = Entry(root, text='username placeholder')
canvas1.create_window(360, 140, window=user)

#Password
password = Label(root, text='Password', font=("Arial", 12))
canvas1.create_window(250, 185, window=password)

password = Entry(root, text='password placeholder')
canvas1.create_window(360, 185, window=password)

#Button
login = Button (root, text='Login',font=("Arial", 14),command=None)
canvas1.create_window(300, 240, window=login)


root.mainloop()

#WIP Finish Backend