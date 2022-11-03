import tkinter as tk
from tkinter import ttk

janela=tk.Tk()

janela.geometry('600x500+100+200')

janela.title('Widget Label')
label1=ttk.Label(
    janela,
    text='Label 1',
    font='Arial 24 bold',
    underline=3,
    cursor='hand1'
)
label1.pack()
   
janela.mainloop()