from tkinter import *

window=Tk()
window.config(bg="white")
window.geometry("600x600")
window.title("Diovanis")

def CalculateBill():
    global total
    total = 0
    if Pizza.get()==1:
        total += 125*int(Pizza_QTY.get() or 0)
    if Burger.get()==1:
        total += 25*int(Burger_QTY.get() or 0)
    if Jello.get()==1:
        total +=  50*int(Jello_QTY.get() or 0)
    if French_Fries.get()==1:
        total +=  12*int(FF_QTY.get()or 0)
    if Burrito.get()==1:
        total +=  15*int(Burrito_QTY.get() or 0)
    if Noodles.get()==1:
        total += 49*int(Noodles_QTY.get() or 0)
    if Taco.get()==1:
        total += 18*int(Taco_QTY.get() or 0)

    MoiTotal.config(text=f'Total Bill: {total}BDT')

def GenerateReceipt():
    Bill.delete("1.0",END)
    Bill.insert(END,"Welcome to Diovanis Resturent")
    Bill.insert(END,"----------------------------------------")
    Bill.insert(END,f"Your Total Bill : {total} BDT")
    Bill.insert(END,"----------------------------------------")
    Bill.insert(END,"Thank You for using our service.")



def Resett():
    Pizza.set(0)
    Burger.set(0)
    French_Fries.set(0)
    Jello.set(0)
    Burrito.set(0)
    Taco.set(0)
    Noodles.set(0)
    Pizza_QTY.delete(0,END)
    Burger_QTY.delete(0,END)
    FF_QTY.delete(0,END)
    Jello_QTY.delete(0,END)
    Burrito_QTY.delete(0,END)
    Taco_QTY.delete(0,END)
    Noodles_QTY.delete(0,END)
    MoiTotal.config(text="Total Bill: 0 BDT")
    Bill.delete("1.0",END)

Menu = Label(text="Select Your Food")
Menu.grid(column=0,row=0,padx=5,pady=5)

Pizza = IntVar()
Burger = IntVar()
French_Fries = IntVar()
Jello = IntVar()
Burrito = IntVar()
Taco = IntVar()
Noodles = IntVar()

Checkbutton(text="Pizza ($125)",variable=Pizza).grid(column=0,row=1)
Checkbutton(text="Burger ($25)",variable=Burger).grid(column=0,row=2)
Checkbutton(text="French Fries ($12)",variable=French_Fries).grid(column=0,row=3)
Checkbutton(text="Jello ($50)",variable=Jello).grid(column=0,row=4)
Checkbutton(text="Burrito ($15)",variable=Burrito).grid(column=0,row=5)
Checkbutton(text="Taco ($18)",variable=Taco).grid(column=0,row=6)
Checkbutton(text="Noodles ($49)",variable=Noodles).grid(column=0,row=7)

Pizza_QTY = Entry()
Pizza_QTY.grid(row=1,column=1)
Burger_QTY = Entry()
Burger_QTY.grid(row=2,column=1)
FF_QTY = Entry()
FF_QTY.grid(row=3,column=1)
Jello_QTY = Entry()
Jello_QTY.grid(row=4,column=1)
Burrito_QTY = Entry()
Burrito_QTY.grid(row=5,column=1)
Taco_QTY=Entry()
Taco_QTY.grid(row=6,column=1)
Noodles_QTY=Entry()
Noodles_QTY.grid(row=7,column=1)

Calculate=Button(text="Calculate Total",command=CalculateBill)
Calculate.grid(row=8,column=0,pady=10)
Receipt=Button(text="Generate Receipt",command=GenerateReceipt)
Receipt.grid(row=8,column=1)
Reset=Button(text="Reset",command=Resett)
Reset.grid(row=8,column=2)

MoiTotal=Label(text="Total Bill Paid: ",font=("Arial",15,"bold")) 
MoiTotal.grid(row=9,column=1)
Bill=Text(width=40,height=10)
Bill.grid(row=10,column=1)

window.mainloop()