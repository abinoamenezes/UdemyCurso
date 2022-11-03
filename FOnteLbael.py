import tkinter as tk
from tkinter import ttk

janela=tk.Tk()

janela.geometry('600x500+100+200')

janela.title('Widget Label')
label1=ttk.Label(
    janela,
    text='Este é um Label\nCurso Python Tkinter',
    font=('Verdana',36,'bold','italic')
    )
label1.pack()

janela.mainloop()