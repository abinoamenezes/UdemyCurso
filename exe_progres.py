from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

from click import progressbar


def messageProgres():
    return f"Progresso atual: {barra['value']}%"

def stop():
    barra.stop()
    laprog['text']=messageProgres()

def aumentar():
    if barra['value']<100:
        barra['value']+=20
        laprog['text']=messageProgres()
    else:
        showinfo(
            title='Aviso',
            message='concluido!'
        )

root=Tk()
root.geometry('600x450+350+120')


barra=ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
barra.grid(column=0, row=0, padx=20,pady=20,columnspan=2)

btpro=Button(
    root,
    text='progresso',
    command=aumentar
)
btpro.grid(column=0,row=2,padx=10,sticky='E')

btstop=Button(
    root,
    text='parar',
    command=stop
    
)
btstop.grid(column=1,row=2,sticky='W',padx=10, pady=10)


laprog=Label(
    root,
    text=messageProgres()
)
laprog.grid(column=0,row=1)

root.mainloop()
