import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task before adding!")

def delete_task():
    try:
        selected_index = task_list.curselection()[0]
        task_list.delete(selected_index)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_list.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.config(bg="#f5f5f5")

title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=("Arial", 12), command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), command=delete_task)
delete_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", font=("Arial", 12), command=save_tasks)
save_button.pack(pady=5)

task_list = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_list.pack(pady=10)

load_tasks()

root.mainloop()