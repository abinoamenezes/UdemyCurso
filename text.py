from distutils.command.config import config
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('text')
text=tk.Text(
    root,
    height=8,
    font='Arial 24',
    background='red',
    foreground='white',
    width=10,  
    
)

text.insert('1.0', 'está é uma caixa de texto')
text.get('1.0','end')


text.pack()

buton=ttk.Button(
    root,
    text='ativa',
    command=lambda: text.config(state='disabled')
)
buton.pack()

buton2=ttk.Button(
    root,
    text='desativar',
    command=lambda: text.config(state='normal')
)
buton2.pack()

root.mainloop()