import tkinter as tk
from tkinter import YView, ttk

root=tk.Tk()
root.title('teste com barra de rolagem')
root.resizable(False,False)
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
texto=tk.Text(
    root,
    width=30,
    height=20
)
texto.grid(column=0,row=0)

barra=ttk.Scrollbar(
    root,
    orient='vertical',
    command=texto.yview
)
barra.grid(column=1,row=0)
texto.config(yscrollcommand=barra.set)

root.mainloop()