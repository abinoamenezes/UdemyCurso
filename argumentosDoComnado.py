import tkinter as tk
from tkinter import ttk
janela=tk.Tk()
janela.title("Minha aplicação GUI")

def select(arg):
    janela.config(background=arg)

janela.geometry('600x500+100+200')
lbl=ttk.Button(
    janela, 
    text='vermelho',
    command=lambda:select('red')
    )
lbl.pack()
lbl2=ttk.Button(
    janela, 
    text='verde',
    command=lambda:select('green')
    )
lbl2.pack()



janela.mainloop()