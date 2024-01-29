from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Log In")

def showPass():
          if var.get()==1:
                    e2.config(show="")
                    e3.config(show="")
          else:
                    e2.config(show="*")
                    e3.config(show="*")
def toLogin():
          root.destroy()
          import login
          

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
                    
                    
def ConfPassOnEnter(e):
          e3.delete(0,"end")
          
def ConfPassOnLeave(e):
          password=e3.get()
          if password == "":
                    e3.insert(0,"Confirm Password")
                    
var =IntVar()


l1=Label(text="Welcome\nSign Up")
l1.configure(font=("Helvetica",20,"bold"))
l1.pack(pady=30)



e1=Entry(width=30,font=(9))
e1.insert(0,"Username")
e1.bind("<FocusIn>",UserOnEnter)
e1.bind("FocusOut",UserOnLeave)
e1.place(x=270,y=190,height=30)


e2=Entry(width=30,font=(9))
e2.insert(0,"Password")
e2.bind("<FocusIn>",PassOnEnter)
e2.bind("<FocusOut>",PassOnLeave)

e2.place(x=270,y=260,height=30)


e3=Entry(width=30,font=(9))
e3.insert(0,"Confirm Password")
e3.bind("<FocusIn>",ConfPassOnEnter)
e3.bind("<FocusOut>",ConfPassOnLeave)
e3.place(x=270,y=330,height=30)

c1=Checkbutton(text="Show Password",command=showPass,variable=var)
c1.place(x=480,y=365)

b1=Button(text="Sign Up",font=(18),height=1,width=20,bg="blue",fg="white",border=0)
b1.place(x=320,y=410)

b2=Button(text="Already have an Account? Log In",bg="white",fg="blue",command=toLogin,border=0)
b2.place(x=320,y=470)







root.mainloop()