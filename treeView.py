from optparse import Values
import tkinter as tk
from tkinter import ttk

from click import command

root = tk.Tk()
root.title('Python Tkinter')
root.geometry('620x300+750+350')

colunas=('nome','sobrenome','idade','telefone')
#criando tabela
table=ttk.Treeview(
    root,
    columns=colunas,
    show='headings'
)

#criando cabeçalho
table.heading('nome',text='Nome')
table.heading('sobrenome',text='Sobrenome')
table.heading('idade',text='Idade')
table.heading('telefone',text='Telefone')

#adicionar dados na tabela

table.insert('', tk.END,values=('Abinoa','Menezes',20,989869414))
table.insert('', tk.END,values=('Janete','Menezes',51,94548122))
table.insert('', tk.END,values=('José','Carlos',52,986927341))

table.grid(row=0,column=0, sticky='nwes')

barra=ttk.Scrollbar(root,orient='vertical', command=table.yview)
table.config(yscroll=barra.set)
barra.grid(row=0,column=1,sticky='ns')

table.column('idade',width=100,anchor='center')


def apagar_item(event):
    for indice in table.selection():
       table.delete(indice)


table.bind('<Return>',apagar_item)

root.mainloop()