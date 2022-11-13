import tkinter as tk
from tkinter import ttk

class rootMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400+150+250')
        self.lbl=ttk.Label(text='Escolha aqui sua opção')
        self.lbl.grid(row=0,column=0,sticky='w')

        self.linguas=('pyhton', 'dart', 'java','C', 'C#')

        self.strva1=tk.StringVar(self)
        self.optMenu=ttk.OptionMenu(
            self,
            self.strva1,
            self.linguas[0],
            *self.linguas
        )
        self.optMenu.grid(column=1,row=0,sticky='w')
    

jan=rootMain()
jan.mainloop()


