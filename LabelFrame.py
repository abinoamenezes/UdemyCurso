
import tkinter as tk
from tkinter import LabelFrame, ttk

root=tk.Tk()
root.geometry('600x400+150+100')

lbl=LabelFrame(
    root,
    text='Marqui aqui',

)
lbl.grid(column=0,row=0,padx=5,pady=5)

rb1=tk.Radiobutton(
    lbl,
    text='Masculino',
    font='Arial 12'
)

rb1.grid(column=0,row=0)

rb2=tk.Radiobutton(
    lbl,
    text='Feminino',
    font='Arial 12'
)

rb2.grid(column=0,row=1)



root.mainloop()