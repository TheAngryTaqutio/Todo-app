
import tkinter as tk
from tkinter import messagebox

with open("todo_list.csv", "r") as file:
    d = dict()

    for line in file:
        line = line.strip('\n')
        (key, val) = line.split(",")
        d[key] = val

#Save files to csv
#Add labels to main tkinter window that gives description of task
#Add option to delete task in list box and csv
#refresh listbox after adding a new item






class Newtodo():
    
    def __init__(self):

        self.nt = tk.Tk()
        self.nt.title("New Task")
        self.nt.geometry("400x100")
        
    
        new_task_lbl = tk.Label(self.nt,text="New Task:")
        new_task_lbl.grid(column=0, row=0)

        self.new_task = tk.Entry(self.nt)
        self.new_task.grid(column=1, row=0, sticky="W")

        desc = tk.Label(self.nt,text="Description")
        desc.grid(column=0, row=1)

        self.desc = tk.Entry(self.nt,width=40)
        self.desc.grid(column=1, row=1, sticky="E")

        #date_lbl = tk.Label(self.nt,text="Complete by:")
        #date_lbl.grid(column=0, row=2)

        #self.date_entry = tk.Entry(self.nt)
        #self.date_entry.grid(column=1, row=2, stick="W")
        
        #Gets values from entry boxes
        

        add_entry = tk.Button(self.nt,text="Add",command =self.add_to_csv)
        add_entry.grid(column=1, row=3)
        

        
        
        
        self.nt.mainloop()

    def add_to_csv(self):
        n = self.new_task.get()
        des= self.desc.get()
        #date = self.date_entry.get()
        
        is_ok = messagebox.askokcancel(title="Enter Task", message=
                                    f"Task: {n} \n"
                                    f"Description: {des} \n"
                                    )
        if is_ok:
            with open("todo_list.csv", "a") as file:
                file.write(f"{n},{des}\n")
            
            self.destroy()

    def destroy(self):
        self.nt.destroy()


        
                
        

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
        self.things = tk.Listbox(width=60,
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
