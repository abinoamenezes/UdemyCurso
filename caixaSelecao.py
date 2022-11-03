import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def mensagem():
    showinfo(
        title='Resultado',
        message=f'Voçê {strVar.get()}'
    )

root=tk.Tk()
root.title('Caixa de seleção')

strVar=tk.StringVar()




caixa=ttk.Checkbutton(
    root,
    text='Eu aceito as condições',
    command=mensagem,
    onvalue='Concorda',
    variable=strVar,
    offvalue='Não concorda'
)
caixa.pack()


root.mainloop()