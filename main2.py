from todo2 import Todos
import tkinter as tk


root = tk.Tk()
app = Todos(root)
list = Todos.create_list(app)





root.mainloop()

