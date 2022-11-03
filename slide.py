import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('GUI')
root.geometry('400x200+650+300')

var=tk.DoubleVar()

def mostrar(event):
    print(var.get())

slide=ttk.Scale(
    root,
    orient='horizontal',
    from_=0,
    to=100,
    variable=var,
    command=mostrar
    )
slide.pack()

root.mainloop()