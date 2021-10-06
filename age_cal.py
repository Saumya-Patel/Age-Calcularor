
from tkinter import *
from datetime import datetime


App = Tk()
App.title("Age Calculator")
App['background'] = 'white'
App.geometry('700x500')


lbl = Label(App, text='Enter Your DOB',  foreground='red', font=('Times', 15))
lbl.grid(row=0, column=3, pady=5)

# Date Label & Entry widget
dateL = Label(App, text='Date:', background='white', foreground='green', font=('Times', 12))
dateE = Entry(App, background='white', foreground='red', width=10)

# Month Label & Entry widget
monL = Label(App, text='Month:', background='white', foreground='green',font=('Times', 12))
monE = Entry(App, background='white', foreground='red', width=10)

# Year Label & Entry widget
yrL = Label(App, text='Year:', background='white', foreground='green',font=('Times', 12))
yrE = Entry(App, background='white', foreground='red', width=10)

# Placing the widgets using grid
dateL.grid(row=1, column=0,pady=5, padx=5)
dateE.grid(row=1, column=1, pady=5, padx=5)
monL.grid(row=1, column=2, pady=5, padx=5)
monE.grid(row=1, column=3, pady=5, padx=5)
yrL.grid(row=1, column=4, pady=5, padx=5)
yrE.grid(row=1, column=5,pady=5, padx=5)



def find_days():
    year = int(yrE.get())
    month = int(monE.get())
    day = int(dateE.get())
    dob = datetime(year=year, month=month, day=day)

    time_now = datetime.now()
    time_dif = time_now - dob
    msg = Label(App, text='You lived ' + str(time_dif.days) + ' days!', background='white',
                foreground='red',font=('Times', 15))
    msg.grid(row=3, column=0, columnspan=3)



def find_sec():
    year = int(yrE.get())
    month = int(monE.get())
    day = int(dateE.get())
    dob = datetime(year=year, month=month, day=day)

    time_now = datetime.now()
    time_dif = time_now - dob
    msg = Label(App, text='You lived ' + str(time_dif.total_seconds()) + ' seconds!', background='white',
                foreground='red',font=('Times', 15))
    msg.grid(row=4, column=0, columnspan=3)



daysB = Button(App, text='Total days', command=find_days, background='green', foreground='white',relief='raised',font=('Times', 12))
scndB = Button(App, text='Total seconds', command=find_sec, background='green', foreground='white',relief='raised',font=('Times', 12))

daysB.grid(row=2, column=0, padx=5, pady=5, columnspan=3)
scndB.grid(row=2, column=3, padx=5, pady=5, columnspan=3)

App.mainloop()

