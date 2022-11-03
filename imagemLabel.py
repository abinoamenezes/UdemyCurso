import tkinter as tk
from tkinter import ttk

janela=tk.Tk()

janela.geometry('600x500+100+200')

janela.title('Widget Label')

foto=tk.PhotoImage(file='/home/abinoa/Downloads/python/UdemyCurso/imagens/tipo-de-arquivo.png')
lbl1=ttk.Label(
    janela,
    image=foto,
    text='Imagem aleatória',
    font='Arial 20',
    compound='left' #bottom left right none text image
)
lbl1.pack()

janela.mainloop()