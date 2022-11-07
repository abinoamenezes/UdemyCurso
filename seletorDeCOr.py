import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor


class RootMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400+150+200')

        ttk.Button(self,text='Clique aqui para abrir um arquivo',command=self.seletor_de_cor).grid(row=1,column=0)

        
    def seletor_de_cor(self):
        cor=askcolor(title='selecione uma cor')
        self.config(bg=cor[1])

        


root=RootMain()
root.mainloop()
