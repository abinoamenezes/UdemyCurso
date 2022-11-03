import tkinter as tk
from tkinter import ttk

janela=tk.Tk()

janela.geometry('600x500+100+200')

janela.title('Widget Label')
label1=ttk.Label(
    janela,
    text='Label temático',
    font='Arial 24',
    borderwidth=10,
    relief=  'groove' #groove, ridge , sunken, raised,flat 
    )
label1.pack()
label2=tk.Label(
    janela,
    text='Label Padrão',
    font='Arial 24',
    borderwidth=10,
    relief=  'groove'
    )
label2.pack()
janela.mainloop()