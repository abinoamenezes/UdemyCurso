import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('GUI')
root.geometry('400x200+650+300')

box1=tk.Label(
    root,
    text='box1',
    background='blue',
    foreground='white'
)

box1.pack(
    ipadx=10,
    ipady=10,
    fill='both',
    expand=True
)
box2=tk.Label(
    root,
    text='box2',
    background='red',
    foreground='white'
   
)
box2.pack(
    ipadx=10,
    ipady=10,
    fill='both',
    expand=True
    
)


root.mainloop()