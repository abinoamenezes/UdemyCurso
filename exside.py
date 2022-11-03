import tkinter as tk

root=tk.Tk()
root.title('exercicio')
root.geometry('700x500+300+150')

lbl1=tk.Label(
    root,
    text='primeiro',
    background='red',
    foreground='white'
   
)

lbl1.pack(
    fill='x',
    ipadx=10,
    ipady=10
)

lbl2=tk.Label(
    root,
    text='segundo',
    background='blue',
    foreground='white'
)

lbl2.pack(
    fill='x',
    ipadx=10,
    ipady=10
)

lbl3=tk.Label(
    root,
    text='Terceiro',
    background='green',
    foreground='white'
)

lbl3.pack(
    fill='x',
    ipadx=10,
    ipady=10
)

lbl4=tk.Label(
    root,
    text='Esquerdo',
    background='pink',
    foreground='white'
)

lbl4.pack(
    expand=True,
    fill='both',
    side='left'

   
)

lbl5=tk.Label(
    root,
    text='Meio',
    background='black',
    foreground='white'
)

lbl5.pack(
    fill='both',
    expand=True,
    side='left'
   
)


root.mainloop()