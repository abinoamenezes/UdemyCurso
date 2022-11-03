import tkinter as tk
from tkinter import ttk
janela=tk.Tk()

def return_pressed(event):
    print('Tecla entre pressionada')

janela.title("Minha aplicação GUI")

janela.geometry('600x500+100+200')

lbl=ttk.Button(janela,text='Executar')
lbl.bind("<Return>",return_pressed)
lbl.focus()
lbl.pack(expand=True)

janela.mainloop()
    