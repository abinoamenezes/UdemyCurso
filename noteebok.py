from tkinter import *
from tkinter import ttk
from tkinter.tix import NoteBook

root=Tk()

root.geometry('600x450+250+120')

note=ttk.Notebook(
    root
)
note.pack()

frame1=Frame(note,width=400,height=280)
frame2=Frame(note,width=400,height=280)

frame1.pack(expand=True,fill='both')
frame2.pack(expand=True,fill='both')
note.add(frame1,text='GUIA 1 ')
note.add(frame2,text='GUIA 2')

button_mostrarGuia1=Button(
    root,
    text='Mostrar guia 1',
    command=lambda:note.add(frame1,text='GUIA 1')
    )

button_mostrarGuia1.pack()

button_mostrarGuia2=Button(
    root,
    text='Mostrar guia 2',
    command=lambda:note.add(frame2,text='GUIA 2')
    )

button_mostrarGuia2.pack()

button_esconderGuia1=Button(
    root,
    text='Esconder guia 1',
    command=lambda:note.hide(0)
    )

button_esconderGuia1.pack()

button_esconderGuia2=Button(
    root,
    text='Esconder guia 2',
    command=lambda:note.hide(1)
    )

button_esconderGuia2.pack()





root.mainloop()