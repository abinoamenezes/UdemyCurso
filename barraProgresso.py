import tkinter as tk
from tkinter import ttk






janela=tk.Tk()

janela.geometry('600x500+100+200')
barra=ttk.Progressbar(
    janela,
    orient='horizontal', #vertical
    length=300,
    mode= 'indeterminate' #indeterminate
)



barra.grid(column=0, row=0,columnspan=2)

buton_ativar=ttk.Button(
    janela,
    text='Ativar',
    command=lambda:barra.start()



)
buton_ativar.grid(row=1,column=0,sticky='E')


button_desativar=ttk.Button(janela,text='Desativar',command=lambda: barra.stop())
button_desativar.grid(row=1, column=1,sticky='W')

janela.mainloop()