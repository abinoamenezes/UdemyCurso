import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('600x400+500+100')

def log(event):
    print('Evento disparado')

lbl=ttk.Button(root,text='Executar')
lbl.bind('<Any-KeyPress>',log)
lbl.focus()
lbl.pack()

lbl2=ttk.Button(
    root,
    text='Desvincular evento de executar',
    command=lambda: lbl.unbind('<Any-KeyPress>')
)
lbl2.pack()

lbl3=ttk.Button(
    root,
    text='Vincular evento de executar',
    command=lambda: lbl.bind('<Any-KeyPress>',log)
)
lbl3.pack()


root.mainloop()