from tkinter import *

__author__ = 'SAI'

cal=Tk()
cal.title('calculator')

def btclick(number):
	global oparetor
	oparetor = oparetor + str(number)
	text_input.set(oparetor)

def btclear():
	global oparetor
	oparetor=""
	text_input.set(" ")

def bteqal():
	global oparetor
	try:
		total=str(eval(oparetor))
		text_input.set(total)
		oparetor=""
	except SyntaxError:
		text_input.set("Math error")
		
oparetor=''
text_input=StringVar()
txt_dispaly=Entry(cal,fg="Black",bg="white",font=('arial',20,'bold'),justify='right',textvariable=text_input,bd=20,width=30).grid(columnspan=9)


b1=Button(cal,text='1',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick(1)).grid(row=1,column=0)
b2=Button(cal,text='2',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick(2)).grid(row=1,column=1)
b3=Button(cal,text='3',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick(3)).grid(row=1,column=2)
b4=Button(cal,text='+',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick('+')).grid(row=1,column=3)
b5=Button(cal,text='4',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick(4)).grid(row=2,column=0)
b6=Button(cal,text='5',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick(5)).grid(row=2,column=1)
b7=Button(cal,text='6',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick(6)).grid(row=2,column=2)
b8=Button(cal,text='-',bg="white",fg="Black",padx=53,pady=50,command=lambda:btclick('-')).grid(row=2,column=3)
b9=Button(cal,text='7',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick('7')).grid(row=3,column=0)
b10=Button(cal,text='8',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick('8')).grid(row=3,column=1)
b11=Button(cal,text='9',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick('9')).grid(row=3,column=2)
b12=Button(cal,text='*',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick('*')).grid(row=3,column=3)
b13=Button(cal,text='0',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick('0/')).grid(row=4,column=0)
b14=Button(cal,text='C',bg="white",fg="Black",padx=50,pady=50,command=btclear).grid(row=4,column=1)
b15=Button(cal,text='=',bg="white",fg="Black",padx=50,pady=50,command=bteqal).grid(row=4,column=2)
b16=Button(cal,text='/',bg="white",fg="Black",padx=50,pady=50,command=lambda:btclick('/')).grid(row=4,column=3)

Label(cal,text="Created By SAI @ G.V.N",fg="Black",justify="center").grid(row=5,column=2,columnspan=3)
cal.mainloop()
