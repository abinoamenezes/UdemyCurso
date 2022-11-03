from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import StringVar, ttk

from click import command

root=tk.Tk()
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

#root.geometry('600x400+300+150')

list=['python','c++','java','javaScript','ruby','php','c','c#']

strr=StringVar(value=list)

listt=tk.Listbox(
    root,
    listvariable=strr,
    height=5,
    selectmode='browse', #extended,
)
listt.grid(column=0,row=0, sticky='nwse')

barra=ttk.Scrollbar(
    root,
    orient='vertical',
    command=listt.yview
)

listt['yscrollcommand']=barra.set
barra.grid(column=1,row=0, sticky='ns')




def retorno(event):
    indices=listt.curselection()
    for i in indices:
        print(listt.get(i))


listt.bind('<<ListboxSelect>>',retorno)





root.mainloop()