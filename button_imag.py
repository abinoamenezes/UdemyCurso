import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from click import command

def downCLick():
    showinfo(
        title='informação',
        message='botao down clicado'
    )

janela=tk.Tk()

janela.geometry('600x500+100+200')

foto=tk.PhotoImage(file='UdemyCurso/imagens/download.png')

janela.title('Widget BUtton')
btn1=ttk.Button(
    janela,
    image=foto,
    command=downCLick
    
   
)

btn1.pack(ipadx=5,ipady=5,expand=True)




janela.mainloop()