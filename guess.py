import random 
from tkinter import * 
root=Tk() 
root.geometry("500x500")
root.config(bg="cyan") 
l1=Label(root,text="Enter the number") 
e1=Entry(root) 
l1.place(x=100,y=120) 
e1.place(x=230,y=120) 
def validate(): 
      x=int(e1.get()) 
      y=random.randint(1,5) 
      if x==y: 
           l2=Label(root,text="Correct guess!") 
           l2.place(x=190,y=250) 
      else:
           l2=Label(root,text="Wrong guess , The correct nulliber is : "+str(y))
           l2.place(x=190,y=250) 
b1=Button(root,text="Guess!",command=validate) 
b1.place(x=180,y=230) 
root.mainloop() 
