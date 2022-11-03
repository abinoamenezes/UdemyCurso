import tkinter as tk
from tkinter import ttk

janela=tk.Tk()

janela.geometry('600x500+100+200')
label=tk.Button(janela, text='oi clássico')
label.pack()
label_tema=ttk.Button(janela,text='oi teemático')
label_tema.pack()


janela.mainloop()