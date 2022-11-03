import tkinter as tk
from tkinter import Button, Label, StringVar, ttk

class calculos:
    @staticmethod
    def convert_far(f):
        fare=(f-32) *5/9    
        return f'{fare:.2f} graus celsius' 
    
    def convert_celsius(c):
        cel=c* 9/5 + 32
        return f'{cel:.2f} farenheit'



class Frame_convert(ttk.Frame):
    def __init__(self,conteiner,texto,convert):
        super().__init__(conteiner)
        self.convert=convert

        self.lbl_fare=ttk.Label(self,text=texto,font='Arial 12',width=9)
        self.lbl_fare.grid(row=0,column=0,padx=2,pady=2)

        self.strvar=StringVar()

        self.entry_fare=ttk.Entry(self,width=20,textvariable=self.strvar)
        self.entry_fare.focus()
        self.entry_fare.grid(row=0,column=1)

        self.btn_convert=Button(self,text='Converter',command=self.mostrar)
        self.btn_convert.grid(row=0,column=2,padx=2)
        
        self.lbl_resposta=Label(self,font='Arial 12')
        self.lbl_resposta.grid(row=1,column=0,columnspan=3)
        self.grid(column=0,row=0)

    
    def mostrar(self,event=None):
        
        self.lbl_resposta['text']=self.convert(float(self.strvar.get()))
    
    def reset(self):
        self.entry_fare.delete(0,tk.END)
        self.lbl_resposta.config(text='')

class ControlFrame(ttk.Labelframe):
    def __init__(self,conteiner):
        super().__init__(conteiner,text='Escolha')

        self.controlValor=tk.IntVar()

        ttk.Radiobutton(
            self,
            text='Celsius to fahrenheit',
            variable=self.controlValor,
            value=0,
            command=self.trocar
        ).grid(row=0,column=0)

        ttk.Radiobutton(
            self,
            text='fahrenheit to celsius',
            variable=self.controlValor,
            value=1,
            command=self.trocar
        ).grid(row=0,column=1)

        self.frame={}
        self.frame[0]=Frame_convert(conteiner,texto='Celsius',convert=calculos.convert_celsius)
        self.frame[1]=Frame_convert(conteiner,texto='Farenheit',convert=calculos.convert_far)
        

        self.grid(row=1,column=0)

        self.trocar()

    def trocar(self):
        frame=self.frame[self.controlValor.get()]
        frame.tkraise()
    
  
class Jan(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('350x120+450+250')
        self.title('Conversor')

root=Jan()
control=ControlFrame(root)

root.mainloop()


