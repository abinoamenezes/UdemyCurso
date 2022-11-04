import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel,WARNING

class RootMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400+150+200')
        ttk.Button(self,text='Clique aqui para fechar a apicação',command=self.fechar_janela).pack()



    def fechar_janela(self):
        x=askokcancel(title='Confirmação',message='Voçê realmente deseja apagar todo os seus dados?',icon=WARNING)
        if x:
            self.destroy()


root=RootMain()
root.mainloop()


