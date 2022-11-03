import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('GUI')
root.geometry('400x200+650+300')


root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
size=ttk.Sizegrip(
    root
)
size.grid(row=1,sticky='SE')

root.mainloop()