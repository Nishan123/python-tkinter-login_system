from tkinter import *
root = Tk()
root.geometry("800x500")
root.title("Login System")

def signup():
          root.destroy()
          import signup
def login():
          root.destroy()
          import login


root.minsize(height=500,width=500)
l1=Label(root,text="Welcome\nGet Started")
l1.pack(pady=50)
l1.configure(font=("Helvetica",20,"bold"))

f1 =Frame()
f1.pack(pady=50)
b1=Button(f1,text="Log In",width=20,command=login)
b1.grid(row=0,column=0)
b2=Button(f1,text="Sign Up",width=20,command=signup)
b2.grid(row=0,column=1,padx=10)


root.mainloop()