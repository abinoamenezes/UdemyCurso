import tkinter as tk
from tkinter import ttk

def button_clicked():
    janela.config(background="blue")
    print('botão clicado')

janela=tk.Tk()
janela.title("Minha aplicação GUI")


janela.geometry('600x500+100+200')
lbl=ttk.Button(janela, text='Clique aqui',command=button_clicked)
lbl.pack()

janela.mainloop()