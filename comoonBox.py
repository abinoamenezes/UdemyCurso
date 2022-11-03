import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root=tk.Tk()
root.geometry('600x500+400+150')

como=ttk.Combobox(
    root,
    values=['Domingo','Segunda','Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
    state='readonly'
)
como.pack(fill='x', pady=5, padx=5)

root.mainloop()