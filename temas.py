import tkinter as tk
from tkinter import ttk

class RootMain (tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x250+200+150')
        self.nome=ttk.Label(self, text='Nome: ')
        self.nome.place(x=5,y= 10)

        self.entry_nome= ttk.Entry(self)
        self.entry_nome.place(x=60,y=10)

        self.button=ttk.Button(self, text='Executar')
        self.button.place(y=10,x=260)

        self.tema=ttk.Label(self, text= 'Tema')
        self.tema.place(x=5,y=45)

root=RootMain()
root.mainloop()