import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Jan(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400+740+220')

        #criando botão
        btn1= ttk.Button(self, text='Clique aqui',command=self.message)
        btn1.pack()

    def message(self):
        showinfo(title='aviso',message='AÍ SIM boy')
        
obj=Jan()
obj.mainloop()

