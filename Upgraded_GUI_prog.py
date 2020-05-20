from tkinter import *
from tkinter import messagebox
from openpyxl import load_workbook
from signing_up import *
from signing_in import *
import smtplib,random

sender = 'techienest.rabia@gmail.com'
password = 'meTechieRabia'
subject = 'OTP for Building Security System' #Line that causes trouble
msg = 'Subject:{}\n\n Your OTP to open Gate1 is '.format(subject)
r= random.randint(10000,99999)
s=''
def Page1():
    global root           
    root = Tk()
    root.title("Building Security System")
    root.geometry("600x400")

        
    F1 = Frame(root)
    F1.pack(side=TOP)
    F2 = Frame(root)
    F2.pack(side=BOTTOM)

        
    def signup(sender,msg,r):
        print("Inside")
        #global root
        root.destroy()
        sign_up(sender,msg,r)


    def signin():
        #global root
        root.destroy()
        sign_in()

    Label(F1,text='Building Security System',font='Helveticca 22 bold italic',width='28',height='2').grid(row=0,column=0)
    Button(F2,text='Sign Up',font='Helveticca 16 bold italic',width='16',height='2',bd=7,command=lambda:signup(sender,msg,r)).grid(row=0,column=0)
    Button(F2,text='Sign In',font='Helveticca 16 bold italic',width='16',height='2',bd=7,command=signin).grid(row=1,column=0)
    Label(F2,text="",font='Helveticca 22 bold italic',width='28',height='2').grid(row=3,column=0)

    root.mainloop()

while(1):
    Page1()
