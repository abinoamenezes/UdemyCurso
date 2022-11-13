import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Menus')
        self.geometry('500x250+750+350')

        self.languages = ('Python', 'JavaScript', 'Java',
                        'Swift', 'GoLang', 'C#', 'C++', 'Scala')
        
        self.option_var = tk.StringVar(self)

        paddings = {'padx': 5, 'pady': 5}

        label = ttk.Label(
            self, 
            text="Selecione sua linguagem favorita"
        )
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.languages[0],
            *self.languages,
            command=self.option_changed
        )
        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)

    def option_changed(self, *args):
        self.output_label["text"] = f"Você selecionou: {self.option_var.get()}"
        
if __name__ == "__main__":
    app = App()
    app.mainloop()