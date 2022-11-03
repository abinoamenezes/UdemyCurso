import tkinter as tk
from tkinter import ttk

from click import command

janela=tk.Tk()

janela.geometry('600x500+100+200')



janela.title('Widget BUtton')
btn1=ttk.Button(
    janela,
    text='Sair',
    command=lambda: janela.quit()
   
)

btn1.pack()

btn2=ttk.Button(
    janela,
    text='Desabilitar',
    command=lambda: btn1.state(['disabled'])
   
)

btn2.pack()

btn3=ttk.Button(
    janela,
    text='Habilitar',
    command=lambda: btn1.state(['!disabled'])
    
   
)

btn3.pack()


janela.mainloop()