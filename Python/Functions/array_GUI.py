import webbrowser
from tkinter import *
from tkinter.ttk import * 
#global variables
G_number_of_students = []
G_waitlist = []
G_number = 1

root = Tk()
root.wm_iconbitmap('icons8-bookmark-48.png')
root.title('Register for class')
root.geometry("500x500")

root.configure(background='white') #How to change the background, image, etc
style = Style() 
style.configure('TButton', font = 
               ('calibri', 20, 'bold'), 
                    borderwidth = '4') 
  
# Changes will be reflected 
# by the movement of mouse. 
style.map('TButton',
        foreground=[('disabled', 'yellow'),
                    ('pressed', 'red'),
                    ('active', 'blue')],
        background=[('disabled', 'magenta'),
                    ('pressed', '!focus', 'cyan'),
                    ('active', 'green')],
        highlightcolor=[('focus', 'green'),
                        ('!focus', 'red')],
        relief=[('pressed', 'groove'),
                ('!pressed', 'ridge')])

def create_list_function():
    global G_number
    if G_number < 6:
        G_number_of_students.append(entry.get())
        print(str(entry.get()) + ' applied to the CSCI with KK - #' + str(G_number))
        print('People registered in the class ' + str(G_number_of_students) +'\n')
        G_number += 1
    else:
        G_waitlist.append(entry.get())
        print(str(entry.get()) + ' is on the waitlist')
        print('People registered in the class'  + str(G_number_of_students))
        print('People on the waitlist ' + str(G_waitlist))
          

def remove_name():
    if entry.get() in G_number_of_students:
        G_number_of_students.remove(entry.get()) #Delete the name
        print(str(entry.get()) + ' has been removed from the list.')
        G_number_of_students.append(G_waitlist[0]) #update name from waitlist to current
        print(G_waitlist[0]+ ' has been moved to current')
        print(G_waitlist[0]+ ' has been moved from waitlist')
        G_waitlist.remove(G_waitlist[0])
        #print(G_waitlist[0]+ ' has been moved from waitlist') #update the G_waitlist to last of in there
        print('People registered in the class ' + str(G_number_of_students))
        print('People on the waitlist ' + str(G_waitlist))
        #G_number_of_students -= 1
    elif entry.get() in G_waitlist:
        G_waitlist.remove(entry.get())
        print('People registered in the class ' + str(G_number_of_students))
        print('People on the waitlist ' + str(G_waitlist))
    else:
        print('Not in the list')
    
def print_list():
    print('People registered in the class ' + str(G_number_of_students))
    print('People on the waitlist ' + str(G_waitlist))
    print() 




label1 = Label(root, text='Enter Name of Student: ',font=('arial', 12,'bold'),background='SteelBlue1')
label1.grid(row=0,column=0)

entry = Entry(root,width=40)
entry.grid(row=0,column=1)

button = Button(root,text='Submit',command=create_list_function)
button.grid(row=1,column=1,columnspan=2,pady=10)

button2 = Button(root,text='Remove',command=remove_name)
button2.grid(row=2,column=1,columnspan=2,pady=10)

button3 = Button(root,text='Show List',command=print_list)
button3.grid(row=3,column=1,columnspan=2,pady=10)

label2 = Label(root, text=str(entry.get()),font=('arial', 24,'bold'),background='red')
label2.grid(row=4,column=1)

root.mainloop()