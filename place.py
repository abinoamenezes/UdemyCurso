import tkinter as tk
from tkinter import Tk, ttk

root= tk.Tk()

root.geometry('600x400+700+300')

lbl1=ttk.Label(
    root,
    text='posição absoluta',
    background='red',
    foreground='white',
    font='Arial 24',
)
lbl1.place(x=20,y=20)

lbl2=ttk.Label(
    root,
    text='posição relativa',
    background='blue',
    foreground='white',
    font='Arial 24',
)
lbl2.place(relx=0.8,y=0.2, anchor='ne', relwidth=0.5)



root.mainloop()