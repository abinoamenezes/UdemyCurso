import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class RootMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400+150+200')
        ttk.Button(self,text='Clique aqui para abrir um arquivo',command=self.abrir_arquivo).pack()

    def abrir_arquivo(self):
        file=filedialog.askopenfilename(
            title='selecione o arquivo',
            initialdir='/', 
            filetypes=(('arquivos texto','*.txt'),('todos os arquivos','*.*'))
            )


root=RootMain()
root.mainloop()
