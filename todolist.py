import tkinter as tk
from tkinter import messagebox
 

def add_task(event=None):
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")


def clear_tasks():
    tasks_listbox.delete(0, tk.END)


def update_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")


root = tk.Tk()
root.title("TO DO LIST")


frame = tk.Frame(root)
frame.pack(pady=100)



tasks_listbox = tk.Listbox(
    frame,
    width=60,
    height=10,
    bd=0,
    selectbackground="red",
    activestyle="none")

tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

task_scrollbar = tk.Scrollbar(frame)
task_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)


tasks_listbox.config(yscrollcommand=task_scrollbar.set)
task_scrollbar.config(command=tasks_listbox.yview)


task_entry = tk.Entry(root, font=("Roboto", 15))
task_entry.pack(pady=20)
task_entry.bind("<Return>", add_task)


task_entry_label = tk.Label(root, text="ENTER A TASK", font=("Roboto", 12))
task_entry_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=20)


add_task_button = tk.Button(button_frame, text="ADD TASK",bg="green" ,fg = "white",activeforeground = "black",activebackground = "black",command=add_task)
add_task_button.pack(side=tk.LEFT, padx=5)


update_task_button = tk.Button(button_frame, text="UPDATE TASK",bg="blue" ,fg = "white",activeforeground = "black",activebackground = "black",command=update_task)
update_task_button.pack(side=tk.LEFT, padx=5)


delete_task_button = tk.Button(button_frame, text="DELETE TASK", bg="red",fg = "white",activeforeground = "black",activebackground = "black",command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=5)

clear_tasks_button = tk.Button(button_frame, text="CLEAR",bg="orange",fg = "white",activeforeground = "black",activebackground = "black", command=clear_tasks)
clear_tasks_button.pack(side=tk.LEFT, padx=5)


root.mainloop()

