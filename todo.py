
import tkinter as tk

with open("todo_list.csv", "r") as file:
    d = dict()

    for line in file:
        line = line.strip('\n')
        (key, val) = line.split(",")
        d[key] = val


class Newtodo(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.new_window.title("New Task")
        self.new_window.geometry("400x100")
    
        new_task_lbl = tk.Label(text="New Task:")
        new_task_lbl.grid(column=0, row=0)

        new_task = tk.Entry()
        new_task.grid(column=1, row=0, sticky="W")

        desc = tk.Label(text="Description")
        desc.grid(column=0, row=1)

        desc = tk.Entry(width=40)
        desc.grid(column=1, row=1, sticky="E")

        date_lbl = tk.Label(text="Complete by:")
        date_lbl.grid(column=0, row=2)

        date_entry = tk.Entry()
        date_entry.grid(column=1, row=2, stick="W")

        add_entry = tk.Button(text="Add")
        add_entry.grid(column=1, row=3)

        self.new_window.mainloop()


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

    def things_todo(self, dict=d):
        things = tk.Listbox(width=60,
                                 height=18,
                                 bg="#afb9e1",
                                 font=8,
                                 highlightbackground="#2893f3",
                                 highlightthickness=0,
                                 )
        for key in d:
            self.things.insert(tk.END, key)

        self.things.grid(column=0, row=0, padx=(5, 0))

    def new_todo(self):
        window = Newtodo()

    def add(self):
        add_item = tk.Button(
            text="Add", width=15, height=11, bg="#7587cb", command=self.new_todo)
        add_item.grid(column=1, row=0, padx=20, pady=20, sticky="N")

    def delete(self):
        delete_item = tk.Button(
            text="Delete", width=15, height=11, bg="#7587cb")
        delete_item.grid(column=1, row=0, sticky="S")
