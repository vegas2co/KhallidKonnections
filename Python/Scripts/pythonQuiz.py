#pythonQuiz
import sqlite3 #database
from tkinter import *
from tkinter.ttk import * 
from tkinter import messagebox
from tkinter import simpledialog
import os
from datetime import date
import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from html.parser import HTMLParser
import webbrowser #open webpage
import json
import requests
import request
from string import Template


sqliteConnection = sqlite3.connect('/Users/khallidwilliams/Library/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/KhallidKonnections.db')

cursor = sqliteConnection.cursor()
d = date.today()

root = Tk() # create window
root.title('Khallid Konnections')
root.geometry('400x600')

canvas1 = Canvas(root, bg='white')
canvas1.pack(fill=BOTH, expand=True)

canvas2 = Canvas(root, bg='white')
canvas2.pack(fill=BOTH, expand=True)

#SCROLL BAR
#yscrollbar=Scrollbar(root, orient=VERTICAL, command=canvas1.yview)
#yscrollbar.pack(side=RIGHT, fill=Y)

imageName1 = PhotoImage(file="/Users/khallidwilliams/Library/Mobile Documents/com~apple~CloudDocs/Desktop/python/server scripts/Python/desktop.gif")
imageName2 = PhotoImage(file="/Users/khallidwilliams/Library/Mobile Documents/com~apple~CloudDocs/Desktop/python/server scripts/Python/pythonLogo.png")
canvas1.create_image(0,0,anchor=NW, image=imageName1)
canvas2.create_image(0,0,anchor=NW, image=imageName2)

style = Style() 
style.configure('TButton', font = 
               ('calibri', 14, 'bold'), 
                    borderwidth = '4') 

style.configure('W.TButton', font = 
               ('calibri', 10, 'bold'), 
                    borderwidth = '1') 
  
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

style.map('W.TButton',
        foreground=[('disabled', 'yellow'),
                    ('pressed', 'blue'),
                    ('active', 'red')],
        background=[('disabled', 'magenta'),
                    ('pressed', '!focus', 'cyan'),
                    ('active', 'green')],
        highlightcolor=[('focus', 'red'),
                        ('!focus', 'green')],
        relief=[('pressed', 'groove'),
                ('!pressed', 'ridge')])

######################### URL FILES PER PAGES ###################################
def syntax():
    url = 'https://www.w3schools.com/python/python_syntax.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('Google', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def variables():
    url = 'https://www.w3schools.com/python/python_variables.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def booleans():
    url = 'https://www.w3schools.com/python/python_booleans.asp'
    #Safari_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def strings():
    url = 'https://www.w3schools.com/python/python_strings.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def numbers():
    url = 'https://www.w3schools.com/python/python_numbers.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def list():
    url = 'https://www.w3schools.com/python/python_lists.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(Safari_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def conditionals():
    url = 'https://www.w3schools.com/python/python_conditions.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def while_loops():
    url = 'https://www.w3schools.com/python/python_while_loops.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def for_loops():
    url = 'https://www.w3schools.com/python/python_for_loops.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def functions():
    url = 'https://www.w3schools.com/python/python_functions.asp'
    f#irefox_path="C:\\Program Files\\Mozilla Safari\\firefox.exe"
    w#ebbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)    
    return a

def userInputs():
    url = 'https://www.w3schools.com/python/python_user_input.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def stringFormatting():
    url = 'https://www.w3schools.com/python/python_string_formatting.asp'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def LearnPython():
    global python_screen
    python_screen = Toplevel(root)
    python_screen.title("Learn Python")
    python_screen.geometry("500x500")
    #imageName1 = PhotoImage(file="pythonLogo.png")
    #python_screen.create_image(0,0,anchor=NW, image=imageName1)
    Label(python_screen, text="Select a topic to begin learning").pack()
    Button(python_screen,text='Syntax', command=syntax).pack()
    Button(python_screen,text='Variables', command=variables).pack()
    Button(python_screen,text='Booleans', command=booleans).pack()
    Button(python_screen,text='Strings', command=strings).pack()
    Button(python_screen,text='Numbers', command=numbers).pack()
    Button(python_screen,text='List', command=list).pack()
    Button(python_screen,text='If...Else', command=conditionals).pack()
    Button(python_screen,text='While Loops', command=while_loops).pack()
    Button(python_screen,text='For Loops', command=for_loops).pack()
    Button(python_screen,text='Functions', command=functions).pack()
    Button(python_screen,text='User Input', command=userInputs).pack()
    Button(python_screen,text='String Formatting', command=stringFormatting).pack()

def contact():
    global fnameEntry
    global lnameEntry
    global emailEntry
    global phoneEntry
    global questionEntry
    global totalEntry
    global python_screen
    python_screen = Toplevel(root)
    python_screen.title("Contact ya boy")
    python_screen.geometry("600x600")
    Label(python_screen, text="Please fill out the form",font = ('calibri', 14, 'bold')).pack()

    ################## First Name #######################
    fname = Label(python_screen, text="First Name:",background='SteelBlue1')
    fname.place(x=130,y=40)
    fnameEntry = Entry(python_screen)
    fnameEntry.place(x=285,y=40)
    #comboBox =Combobox(python_screen, text="Khallid Konnections").pack(side=TOP)
    ################## Last Name #######################
    lname = Label(python_screen, text="Last Name:",background='SteelBlue1')
    lname.place(x=130,y=80)
    lnameEntry = Entry(python_screen)
    lnameEntry.place(x=285,y=80)
    ################## Email Address #######################
    email = Label(python_screen, text="Email:",background='SteelBlue1')
    email.place(x=130,y=120)
    emailEntry = Entry(python_screen)
    emailEntry.place(x=285,y=120)
    ################## Phone Number #######################
    phone = Label(python_screen, text="Phone Number:",background='SteelBlue1')
    phone.place(x=130,y=160)
    phoneEntry = Entry(python_screen)
    phoneEntry.place(x=285,y=160)
    ################## Question #######################
    question = Label(python_screen, text="Question:",background='SteelBlue1')
    question.place(x=130,y=200)
    questionEntry = Text(python_screen,font = ('calibri', 14, 'bold'),background='light grey')
    questionEntry.place(x=285,y=200,height=200,width=200)
    ################## Total #######################
    total = Label(python_screen, text="Total:",background='SteelBlue1')
    total.place(x=130,y=440)
    totalEntry = Entry(python_screen)
    totalEntry.place(x=285,y=440)
    ################## Submit #######################
    submit = Button(python_screen, text='Submit',command=saveToDatabase)
    submit.place(x=200,y=520)

def installPython():
    url = 'https://www.python.org/'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a

def installVB():
    url = 'https://code.visualstudio.com/'
    #firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    a = webbrowser.get('Safari').open_new_tab(url)
    return a
    
######################### Appplications ###################################

def ExitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        pass

def NumbersQuiz():
    count = 0
    MsgBox = messagebox.askquestion ('Number Quiz','Are you ready to begin the Numbers Quiz?',icon= 'warning')
    if MsgBox == 'yes':
        ######################### Question 1 ###################################
        answer1 = simpledialog.askinteger("Question 1", " apple = 5 \n banana = 10 \n total = apple + banana \n\n\n total = ?",parent=root)
        if answer1 == 15:
            messagebox.showinfo('Answer', 'Good Job! The answer is 15 \nYour answer is '+ str(answer1))
            count += 1
        else:
            messagebox.showerror('Answer', 'The correct answer is 15 \nYour answer is '+ str(answer1))
        ######################### Question 2 ###################################
        answer2 = simpledialog.askinteger("Question 2", "a = 1 \nb = 4 \nc = 8 \nd = c - b - a \nprint(d) \n\n\nWhat is the output?",parent=root)
        if answer2 == 3:
            messagebox.showinfo('Answer', 'Good job! The answer is 3 \nYour answer is '+ str(answer2))
            count += 1
        else:
            messagebox.showerror('Answer', 'The correct answer is 3 \nYour answer is '+ str(answer2))

        messagebox.showinfo('Results', 'Total correct were ' + str(count) + '/2\n\n Percentage= '+str((count*100)/2)+'%')

def StringQuiz():
    count = 0
    MsgBox = messagebox.askquestion ('String Quiz','Are you ready to begin the Strings Quiz?',icon= 'warning')
    if MsgBox == 'yes':
        ######################### Question 1 ###################################
        answer1 = simpledialog.askstring("Question 1", "firstName = 'Mickey' \nlastName = 'Mouse' \nfullName = firstName + lastName \nprint(fullName) \n\n\n\n\nWhat is the output?",parent=root)
        if answer1 == 'MickeyMouse':
            messagebox.showinfo('Answer', 'Correct the answer is ' +answer1)
            count += 1
        else:
            messagebox.showerror('Answer', 'The correct answer is '+'MickeyMouse\n'+'Your answer is '+ answer1)

        ######################### Question 2 ###################################
        answer2 = simpledialog.askstring("Question 2 Concatenation", "a = 'Apple' \nb = 'Banana' \nc = 'Cherry' \nd = c + ' ' + b + ' ' + a \nprint(d) \n\n\n\n\nWhat is the output?",parent=root)
        if answer2 == 'Apple Banana Cherry':
            messagebox.showinfo('Answer', 'Correct the answer is '+answer2)
            count += 1
        else:
            messagebox.showerror('Answer', 'The correct answer is '+'Apple Banana Cherry\n'+'Your answer is '+ answer2)

        ######################### Question 3 ###################################
        answer3 = simpledialog.askstring("Question 3", "text = 'Hello World' \nprint(txt[6]) \n\n\n\nWhat is the output?",parent=root)
        if answer3 == 'W':
            messagebox.showinfo('Answer', 'Correct the answer is '+answer3)
            count += 1
        else:
            messagebox.showerror('Answer', 'The correct answer is '+'W\n'+'Your answer is '+ answer3)

        ######################### Question 4 ###################################
        answer4 = simpledialog.askstring("Question 4", "a = 'Hello World' \nprint(a.replace('H', 'J')) \n\n\n\nWhat is the output?",parent=root)
        if answer4 == 'Jello World':
            messagebox.showinfo('Answer', 'Correct the answer is '+answer4)
            count += 1
        else:
            messagebox.showerror('Answer', 'The correct answer is '+'Jello World\n'+'Your answer is '+ answer4)

        ######################### Question 5 ###################################
        answer5 = simpledialog.askstring("Question 5", "a = 'Hello' \nb = 'World' \nc = '{} {}' \nprint(c.format(a,b)) \n\n\n\nWhat is the output?",parent=root)
        if answer5 == 'Hello World':
            messagebox.showinfo('Answer', 'Correct the answer is '+answer5)
            count += 1
        else:
            messagebox.showerror('Answer', 'The correct answer is '+'MickeyMouse\n'+'Your answer is '+ answer5)
        
        ######################### Results ###################################
        messagebox.showinfo('Results', 'Total correct were ' + str(count) + '/5\n\n Percentage= '+str((count*100)/5)+'%')

######################### Daily Report Function ###################################
def getDailyReportFromDataBase():
    try:
        cursor.execute("select [Last Name] from pythonToQuiz where Date = " + str(d))
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
            return x
    except sqlite3.Error as error:
        print("Error while inserting Data to a sqlite table", error)

######################### Save to Text File Function ###################################
def saveToTextFile():
    array = []
    text_file = open(os.path.expanduser('email_'+str(d)+'.txt'),'a')
    try:
        cursor.execute("select [Total] from pythonToQuiz")
        myresult = cursor.fetchall()
        for x in myresult:
            array.append(x)
            print(x)
        text_file.write(str(array[0:]) + '\n\n' + 'Daily Total ')
        text_file.close()
        print('Added to Text File')
    except sqlite3.Error as error:
        print("Error while inserting Data to a sqlite table", error)

def saveToCSVFile():
    pass
    
######################### Save to Databse Function ###################################
def saveToDatabase(): #Database function
    fn = fnameEntry.get()
    ln = lnameEntry.get()
    en = emailEntry.get()
    pn = phoneEntry.get()
    qn = questionEntry.get("1.0",END)
    tot = totalEntry.get()

    MsgBox = messagebox.askquestion ('Are you sure?','Is all the data accurate?',icon = 'warning')
    if MsgBox == 'yes':
        try:
            cursor.execute('''
            insert into pythonToQuiz
            ([First Name], [Last Name], [Email], [Phone Number], [Questions], [Date], [Total])
            VALUES(?,?,?,?,?,?,?)
            ''',
            (fn,ln,en,pn,qn,d,tot)
            )
            
            sqliteConnection.commit()
            print("Successfully Saved Information")
            print('First Name: ' + fn + '\n' + 
            'Last Name: ' + ln + '\n' + 
            'Email: ' + en + '\n' + 
            'Phone Number: ' + pn + '\n' +
            'Question: ' + qn + '\n' +
            'Total: ' + tot + '\n' +
            'Date: ' + str(d))

            fnameEntry.delete(0,END)
            lnameEntry.delete(0,END)
            emailEntry.delete(0,END)
            phoneEntry.delete(0,END)
            totalEntry.delete(0,END)
            #questionEntry.delete(0,END)
           
        except sqlite3.Error as error:
            print("Error while inserting Data to a sqlite table", error)

        messagebox.showinfo('Khallid Konnections','Data submitted to Khallid Konnections. We will contact you ASAP!')
        saveToTextFile() #saves to text file        

button1 = Button (root, text='Exit Application',command=ExitApplication)
canvas1.create_window(200, 180, window=button1)

button3 = Button (root, text='Number Quiz',command=NumbersQuiz)
canvas1.create_window(200, 100, window=button3)

button4 = Button (root, text='String Quiz',command=StringQuiz)
canvas1.create_window(200, 140, window=button4)

button5 = Button (root, text='Learn Python', command=LearnPython)
canvas2.create_window(200, 100, window=button5)

button5 = Button (root, text='Contact Khallid Konnections', command=contact)
canvas2.create_window(200, 140, window=button5)

button6 = Button (root, text='Install Python', command=installPython)
canvas2.create_window(60, 30, window=button6)

button7 = Button (root,  text='Install Visual Studio',  command=installVB)
canvas2.create_window(300, 30, window=button7)
  
root.mainloop()