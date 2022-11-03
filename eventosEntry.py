from curses.textpad import Textbox
from pickle import NONE
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root=tk.Tk()
root.title('Meu app')
root.geometry('600x400+350+150')

def mensagem(event):
    if texto.get()!='Insira seu nome...':
        showinfo(
            title='informação...',
            message=f'Bem-Vindo(a) {texto.get()}'
        )
        texto.set('Insira seu nome...')
        textBox.select_range(0,tk.END)
        textBox.focus()
    else:
        showinfo(
            title='informação...',
            message='Você digitou nada arrombado burrooooo'
        )



texto=tk.StringVar()
texto.set('Insira seu nome...')

textBox=ttk.Entry(
    root,
    textvariable=texto,
    font='Arial 24 italic'

)

textBox.select_range(0,tk.END)
textBox.focus()
textBox.bind('<Return>',mensagem)
textBox.pack()


btn1=ttk.Button(
    root,
    text='Executar',
    command=lambda:mensagem(None)
    
)

btn1.pack()
root.mainloop()