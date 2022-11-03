
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Python Tkinter')
root.geometry('620x300+750+350')

table=ttk.Treeview(
    root,
    columns=('departamentos'),
    show='headings'
)

table.heading('departamentos',text='Departamentos')

table.insert('',tk.END,values=('TI'),iid=0,open=False)
table.insert('0',tk.END,values=('Funcionários'),iid=1,open=False)
table.insert('1',tk.END,values=('Abinoã'),iid=2,open=False)
table.insert('',tk.END,values=('ADM'),iid=4,open=False)

table.move(1,4,tk.END)

table.grid(row=0,column=0)


root.mainloop()