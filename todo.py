
import tkinter as tk

with open("todo_list.csv","r") as file:
    d = dict()
    
    for line in file:
        line = line.strip('\n')
        (key, val) = line.split(",")
        d[key] = val
print(d)

class Todo(tk.Tk):
    def __init__(self):
        
        super().__init__()

        
        self.window()
        

    def window(self):
        self.geometry("700x425")
        self.config(bg="#35478C")
        
        self.things_todo()
        self.add()
        self.delete()
    

    def things_todo(self,dict=d):
        self.things = tk.Listbox(width=60,
                                 height=18,
                                 bg="#afb9e1",
                                 font=8,
                                 highlightbackground="#2893f3",
                                 highlightthickness=0,
                                 )
        for key in d:
            self.things.insert(tk.END, key)
        
        self.things.grid(column=0, row=0,padx=(5,0))

    def add(self):
        self.add_item = tk.Button(text="Add", width=15, height=11, bg="#7587cb")
        self.add_item.grid(column=1, row=0,padx=20,pady=20, sticky="N")

    def delete(self):
        self.delete_item = tk.Button(text= "Delete", width=15, height=11, bg="#7587cb")
        self.delete_item.grid(column=1, row=0, sticky="S")
    





