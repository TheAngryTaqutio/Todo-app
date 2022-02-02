
import tkinter as tk
from tkinter import messagebox
import pandas as pd



# Create a todo list class


class Todos:

    # Create an init that sets up tk window
    def __init__(self, master):
        self.master = master
        master.geometry("700x425")
        master.title("ToDo App")

        add_item = tk.Button(master,
                             text="Add",
                             width=15,
                             height=11,
                             bg="#7587cb",
                             command=self.new_task)
        
        add_item.grid(column=1,
                      row=0,
                      padx=20,
                      pady=20,
                      sticky="N")

        delete_item = tk.Button(master,
                                text="Delete",
                                width=15,
                                height=11,
                                bg="#7587cb",
                                command=self.delete)


        delete_item.grid(column=1,
                         row=0,
                         sticky="S",)

    # Create a listbox to display you things todo

    def create_list(self):
    # create a csv file to store todos along with a description
        try:
            with open("todo_list.csv", "r") as file:
                self.d = dict()

                for line in file:
                    line = line.strip('\n')
                    (key, val) = line.split(",")
                    self.d[key] = val
        except:
            with open("todo_list.csv", "w") as file:
                self.d = dict()

        self.things = tk.Listbox(self.master,
                                 width=60,
                                 height=18,
                                 bg="#afb9e1",
                                 font=8,
                                 highlightbackground="#2893f3",
                                 highlightthickness=0)
        for key in self.d:
            if key != "task":
                self.things.insert(tk.END, key)




        self.things.grid(column=0,
                         row=0,
                         padx=(5, 0))

    # Create the ablility to add a new task
    def new_task(self):
        self.new = tk.Toplevel(self.master,width=400, height=100)
        
        new_task_lbl = tk.Label(self.new,text="New Task:")
        new_task_lbl.grid(column=0, row=0)

        self.new_task = tk.Entry(self.new)
        self.new_task.grid(column=1, row=0, sticky="W")

        desc_lbl = tk.Label(self.new,text="Description")
        desc_lbl.grid(column=0, row=1)

        self.desc = tk.Entry(self.new,
                             width=40)
        
        self.desc.grid(column=1,
                       row=1,
                       sticky="E")
        
        
        
        add_entry = tk.Button(self.new,
                              text="Add",
                              command=self.add)
        add_entry.grid(column=1,
                       row=3)
        
    def add(self):
        n = self.new_task.get()
        des = self.desc.get()
        
        self.d[n]= des
        
        is_ok = messagebox.askokcancel(title="Enter Task", message=
                                    f"Task: {n} \n"
                                    f"Description: {des} \n"
                                    )
        if is_ok:
            with open("todo_list.csv", "a") as file:
                file.write(f"{n},{des}\n")
            
            self.things.insert(tk.END, n)
            
            self.new.destroy()
# Create the ability to delete task from todolist   

    def delete(self):
        df = pd.read_csv("todo_list.csv")
        
        delete_todo = messagebox.askokcancel(title="Delete Todo task",
                                             message=f"Delete {self.things.get(self.things.curselection())}")
        if delete_todo:
            drop = self.things.get(self.things.curselection())
            self.things.delete(self.things.curselection())
           
            with open("todo_list.csv", "r") as file:
                lines = file.readlines()
            with open("todo_list.csv", "w") as file:
                for line in lines:
                    if drop not in line:
                        file.write(line)
    



            
        

            


    # Display the todo item along with a description

    