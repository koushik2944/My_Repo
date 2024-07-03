from tkinter import *

window = Tk()


def kg_to_ounces():
    grm = float(e2_value.get()) * 1000
    pnd = float(e2_value.get()) * 2.20462
    oun = float(e2_value.get()) * 35.274
    t1.insert(END, grm)
    t2.insert(END, pnd)
    t3.insert(END, oun)


e1 = Label(window, text="Kg")
e1.grid(row=0, column=0)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=kg_to_ounces)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()