import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Entry')
root.geometry('600x400+350+150')

texto=tk.StringVar()
texto.set('insira seu nome...')

textBox=ttk.Entry(
    root,
    textvariable=texto,
    font='Arial 24 italic'

)
textBox.select_range(0,tk.END)
textBox.focus()
textBox.pack()

btn1=ttk.Button(
    root,
    text='Executar',
    command=lambda:print(texto.get())
)

btn1.pack()
root.mainloop()