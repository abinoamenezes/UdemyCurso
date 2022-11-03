import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Login')
root.geometry('300x250+150+100')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

username=ttk.Label(root,text='Username:')
username.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry=ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E,padx=5,pady=5)

senha_label=ttk.Label(root, text='Senha:')
senha_label.grid(column=0, row=1, sticky=tk.W,padx=5, pady=5)

senha_entry=ttk.Entry(root, show='*')
senha_entry.grid(column=1,row=1, sticky=tk.E,padx=5,pady=5)

button_login=ttk.Button(root, text='Login')
button_login.grid(column=1, row=3, sticky=tk.E, padx=5,pady=5)



root.mainloop()