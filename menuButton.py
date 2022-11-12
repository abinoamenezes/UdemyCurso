import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Menús')
        self.geometry('500x250+750+350')


        #criando menuBUtton

        menubutton=ttk.Menubutton(self,text='selecine uma opção')
        
        
        #criando um menu que será adicionado ao menuButton
        strvar=tk.StringVar()
        menu=tk.Menu(menubutton)
        menu.add_radiobutton(label='cor',variable=strvar)
        menu.add_radiobutton(label='mese',variable=strvar)

        menubutton.configure(menu=menu)

        menubutton.pack()
root=App()
root.mainloop()