import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from turtle import title


class Fra(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)

        btn=ttk.Button(self,text='clique aqui',command=self.message)
        btn.pack()
        self.pack()

    def message(self):
        showinfo(title='aviso',message='IAEEEEEE')
    



class Jan(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x250+350+250')
        


root=Jan()
frame=Fra(root)
root.mainloop()
