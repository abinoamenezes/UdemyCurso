import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

class rootMain(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('600x400')


        ttk.Button(
            self,
            text='Aviso',
            command=lambda:showwarning(title='Aviso',message='Esse é um aviso')
            ).pack()
        
        ttk.Button(
            self,
            text='informação',
            command=lambda:showinfo(title='Informação',message='Essa é uma informação')
        ).pack()

        ttk.Button(
            self,
            text='error',
            command=lambda:showerror(title='Erro',message='Esse é um erro')
        ).pack()

root=rootMain()
root.mainloop()
