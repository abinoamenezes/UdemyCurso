import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('600x400+150+100')

frame1=ttk.Frame(
    root,
    width=600,
    height=400,
    borderwidth=5,
    relief='solid',
    padding=(10,50,10,50)

)
frame1.pack()

lbl1=ttk.Label(frame1,text='estou dentro', background='yellow')
lbl1.pack()


lbl2=ttk.Label(frame1,text='estou dentro tbm', background='red')
lbl2.pack()

root.mainloop()