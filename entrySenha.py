import tkinter as tk
from tkinter import ttk

janela=tk.Tk()
janela.geometry('600x400+650+150')

textbox=ttk.Entry(
    janela,
    show='+'

)
textbox.focus()
textbox.pack()

btn1=ttk.Button(
    janela,
    text='Executar',
    command=lambda: print(textbox.get())
)
btn1.pack()

janela.mainloop()