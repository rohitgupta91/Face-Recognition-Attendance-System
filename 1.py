from tkinter import *

win = Tk()


# This Entry widget will accept the password from user.
pas = Entry(win, show = "*")
pas.place(x = 70,y = 0)


lab = Label(win, text = "Password :")
lab.place(x = 0, y = 0)

def mark() :

    if var.get() == 1 :
        pas.configure(show = "")
    elif var.get() == 0 :
        pas.configure(show = "*")

var = IntVar()


# I have used check button for my convenience. 

# This will help us to to enable or disable the hiding the password.  
bt = Checkbutton(win, command = mark, offvalue = 0, onvalue = 1, variable = var)
bt.place(x = 170, y = 0)

win.mainloop()



