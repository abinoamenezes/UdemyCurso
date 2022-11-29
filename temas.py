import tkinter as tk
from tkinter import ttk

class RootMain (tk.Tk):
    def __init__(self):
        super.__init__()
        self.nome=ttk.Label(self, text='Nome: ')
        self.nome.place(x=5,y= 10)



root=RootMain()
root.mainloop()