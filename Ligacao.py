import tkinter as tk
from tkinter import ttk

def log(event):
    print(event)



janela=tk.Tk()
janela.title("Minha aplicação GUI")
lbl=tk.Button(janela,text="Executar 1")
lbl.focus()
janela.bind_class('Button', '<Any-KeyPress>',log)
lbl.pack()


lbl2=tk.Button(janela,text='Excutar 2')
lbl2.pack()

lbl3=tk.Button(janela,text='Executar 3')
lbl3.pack()

janela.geometry('600x500+100+200')


janela.mainloop()