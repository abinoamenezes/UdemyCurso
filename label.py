import tkinter as tk
from tkinter import ttk

janela=tk.Tk()

janela.geometry('600x500+100+200')

janela.title('Widget Label')
label1=ttk.Label(
    janela,
    text='Este é um Label\nCurso Python Tkinter',
    background='yellow',
    foreground='red',
    padding=20,
    width=15,
    justify='right',
    anchor='center'
    )
label1.pack()

janela.mainloop()