import tkinter as tk
from tkinter import ttk

janela=tk.Tk()
janela.title("Minha aplicação GUI")
janela.geometry('600x500+100+200')

label=ttk.Label(janela)
label["text"]='olá mundo'

label.pack()

lbl=ttk.Label(janela)
lbl.config(text='Olá mundo 2')
lbl.pack()

janela.mainloop()