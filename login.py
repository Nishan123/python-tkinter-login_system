from tkinter import *
import string
from tkinter import messagebox
root = Tk()
root.geometry("800x500")
root.title("Log In")

def signUp():
          root.destroy()
          import signup

def showPass():
          if var.get()==1:
                    e2.config(show="")
          else:
                    e2.config(show="*")
def onLogin():
          
         special_char = list(string.punctuation)
         username = e1.get()
         password = e2.get()

         if len(username)<8:
                   print("Email must be 8 char long")
         elif "@gmail.com" not in username:
                   print("Must provide domain")
         elif len(password)<8:
                   print("Password must be 8 char long ")
         else:
                   for i in range(len(special_char)):
                            
                             if any(char in special_char for char in password):
                                           print("Successfully logged in")
                                           break
                             else:
                                        print("Password must contain special char")
                                        break
                                       
                                        
                                        
          
def UserOnEnter(e):
          e1.delete(0,"end")
          
def UserOnLeave(e):
          username=e1.get()
          if username == "":
                    e1.insert(0,"Username")
                    
                    
                    
                    
                    
def PassOnEnter(e):
          e2.delete(0,"end")
          
def PassOnLeave(e):
          password=e2.get()
          if password == "":
                    e2.insert(0,"Password")
          
            
var =IntVar()

welcome = Label(text="Welcome Back",font=("Helvetica",20,'bold')).place(x=350,y=40)

e1=Entry(width=30,font=(9))
e1.insert(0,"Username")
e1.bind("<FocusIn>",UserOnEnter)
e1.bind("FocusOut",UserOnLeave)
e1.place(x=270,y=180,height=30)


e2=Entry(width=30,font=(9))
e2.insert(0,"Password")
e2.bind("<FocusIn>",PassOnEnter)
e2.bind("<FocusOut>",PassOnLeave)
e2.place(x=270,y=250,height=30)

c1=Checkbutton(text="Show Password",command=showPass,variable=var)
c1.place(x=480,y=300)

b1=Button(text="Log In",font=(18),height=1,width=20,bg="blue",fg="white",command=onLogin,border=0)
b1.place(x=320,y=350)
b2=Button(text="Dont have an account? Sign Up",bg="white",fg="blue",command=signUp,border=0)
b2.place(x=320,y=470)


root.mainloop()