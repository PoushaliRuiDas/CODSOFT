import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all():
    listbox.delete(0, tk.END)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("todo_list.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Create the main application window
app = tk.Tk()
app.title("To-Do List Application")

# Create and configure the widgets
label = tk.Label(app, text="Enter task:")
entry = tk.Entry(app, width=40)
add_button = tk.Button(app, text="Add Task", command=add_task)
delete_button = tk.Button(app, text="Delete Task", command=delete_task)
clear_button = tk.Button(app, text="Clear All", command=clear_all)
save_button = tk.Button(app, text="Save Tasks", command=save_tasks)
listbox = tk.Listbox(app, width=50)

# Grid layout for widgets
label.grid(row=0, column=0, padx=10, pady=5)
entry.grid(row=0, column=1, padx=10, pady=5)
add_button.grid(row=1, column=0, padx=10, pady=5)
delete_button.grid(row=1, column=1, padx=10, pady=5)
clear_button.grid(row=1, column=2, padx=10, pady=5)
save_button.grid(row=1, column=3, padx=10, pady=5)
listbox.grid(row=2, column=0, columnspan=5, padx=10, pady=5)

# Start the main event loop
app.mainloop()
