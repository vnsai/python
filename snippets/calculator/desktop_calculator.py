from tkinter import *

__author__ = 'SAI'

oparetor = ""

def btclick(number):
    global oparetor
    oparetor = oparetor + str(number)
    result.set(oparetor)

def total():
    global oparetor
    try:
        totale = float(eval(oparetor))
        result.set(totale)
        oparetor=""
    except SyntaxError:
        result.set("Syntex Error")

def btclear():
    global oparetor
    oparetor = ""
    result.set(oparetor)
    
r=Tk()
r.title("Calculator @SAI")
result=StringVar()
Entry(r,textvariable=result,bd=5,fg="Black",bg="black",justify="right",font=("arial",20,"bold"),state="readonly").grid(row=0,column=0,columnspan=4)

Button(r,text="CE",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=btclear).grid(row=1,column=0)
Button(r,text="RM",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=btclear).grid(row=1,column=1)
Button(r,text="(",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick("(")).grid(row=1,column=2)
Button(r,text=")",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(")")).grid(row=1,column=3)

Button(r,text="7",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(7)).grid(row=2,column=0)
Button(r,text="8",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(8)).grid(row=2,column=1)
Button(r,text="9",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(9)).grid(row=2,column=2)
Button(r,text="+",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick('+')).grid(row=2,column=3)

Button(r,text="4",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(4)).grid(row=3,column=0)
Button(r,text="5",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(5)).grid(row=3,column=1)
Button(r,text="6",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(6)).grid(row=3,column=2)
Button(r,text="-",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick('-')).grid(row=3,column=3)

Button(r,text="1",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(1)).grid(row=4,column=0)
Button(r,text="2",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(2)).grid(row=4,column=1)
Button(r,text="3",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(3)).grid(row=4,column=2)
Button(r,text="*",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick('*')).grid(row=4,column=3)

Button(r,text="0",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(0)).grid(row=5,column=0)
Button(r,text=".",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick(".")).grid(row=5,column=1)
Button(r,text="=",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=total).grid(row=5,column=2)
Button(r,text="/",width=7,height=2,font=("arial",10,"bold"),fg="Black",command=lambda:btclick('/')).grid(row=5,column=3)

Label(r,text="CREATED BY SAI @ G.V.N",font=("arial",7,"bold"),fg="Black").grid(row=6,column=0,columnspan=4)
r.mainloop()
