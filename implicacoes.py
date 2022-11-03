import tkinter as tk
from tkinter import ttk

janela=tk.Tk()

janela.geometry('600x500+100+200')

janela.title('Widget Label')
label1=ttk.Label(
    janela,
    text='0123456789',
    font='Arial 24',
    borderwidth=1,
    relief=  'solid', #groove, ridge , sunken, raised,flat 
    #width=5,
    wraplength=100
    )
label1.pack()
label2=tk.Label(
    janela,
    text='0123456789\n0123456789',
    font='Arial 24',
    borderwidth=1,
    relief=  'solid',
    #width=5,
    #height=2
    wraplength=100
    )
label2.pack()
janela.mainloop()