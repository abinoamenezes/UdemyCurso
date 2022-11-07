import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo

class RootMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400+150+200')

        ttk.Button(self,text='Clique aqui para abrir um arquivo',command=self.abrir_arquivo).grid(row=1,column=0)

        self.text=tk.Text(width=80,height=20)
        self.text.grid(row=0,column=0)

    def abrir_arquivo(self):
        file=filedialog.askopenfile(
            title='selecione o arquivo',
            initialdir='/', 
            filetypes=(('arquivos texto','*.txt'),('todos os arquivos','*.*'))
            )

        self.text.delete('1.0','end')
        for linha in file.readlines():
            self.text.insert('1.0', linha)
       


root=RootMain()
root.mainloop()
