
import tkinter as tk


class Todo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window()

    def window(self):
        self.geometry("700x300")
        self.config(bg="#35478C")
        self.things_todo()
        self.add()
        self.delete()
    

    def things_todo(self):
        self.things = tk.Listbox(width=100,
                                 height=20,
                                 bg="#1355a4",
                                 highlightbackground="#2893f3",
                                 highlightthickness=0)
        
        self.things.grid(column=0, row=0)

    def add(self):
        self.add_item = tk.Button(text="Add", width=15, height=9)
        self.add_item.grid(column=1, row=0, sticky="N")

    def delete(self):
        self.delete_item = tk.Button(text= "Delete", width=15, height=9)
        self.delete_item.grid(column=1, row=0, sticky="S")
    





