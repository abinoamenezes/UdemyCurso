import tkinter as tk
from tkinter import Spinbox, ttk

root=tk.Tk()
root.geometry('600x400+150+100')

spin=Spinbox(
    root,
    from_=0,
    to=10,
    wrap=True,
    values=(12,13,22,45)
)

spin.pack()
root.mainloop()