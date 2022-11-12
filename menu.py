import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Menús')
        self.geometry('500x250+750+350')

        #criando barra de menu
        menubar=tk.Menu(self)
        self.configure(menu=menubar)

        #criando menus
        menu_opcoes=tk.Menu(menubar,tearoff=False)
        menu_informações=tk.Menu(menubar,tearoff=False)

        #adicionar comando aos menus
        menu_opcoes.add_command(label='abrir seletor de cores')
        menu_opcoes.add_command(label='sair')

        menu_informações.add_command(label='informações sobre o desenvolvedor')

        menubar.add_cascade(label='opçoes',menu=menu_opcoes,underline=0)
        menubar.add_cascade(label='informações', menu=menu_informações)

        #criando submenu
        sub_menu=tk.Menu(menu_opcoes)
        sub_menu.add_command(label='informações adicionais')
        menu_opcoes.add_cascade(label='mais',menu=sub_menu)

root=App()
root.mainloop()