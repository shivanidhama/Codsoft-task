import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
from datetime import datetime

# Empty list to store tasks
tasks = []

# Function to update the task display
def update_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, f"{task['text']} (Added: {task['time']})")

# Add new task
def add_task():
    task_text = entry.get().strip()
    if task_text:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks.append({"text": task_text, "time": time_now})
        update_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("No Task", "Please enter a task.")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_tasks()
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

# Clear all tasks
def clear_tasks():
    if messagebox.askyesno("Are you sure?", "Clear all tasks?"):
        tasks.clear()
        update_tasks()

# Save tasks to a file
def save_tasks():
    file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                             filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            json.dump(tasks, f)
        messagebox.showinfo("Saved", "Tasks saved successfully.")

# Load tasks from a file
def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path and os.path.exists(file_path):
        with open(file_path, "r") as f:
            global tasks
            tasks = json.load(f)
        update_tasks()

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="#f0f0f0")

# Entry
entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task, width=20).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task, width=20).pack(pady=5)
tk.Button(root, text="Clear All", command=clear_tasks, width=20).pack(pady=5)

# Listbox to show tasks
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=20)

# Save/Load buttons
tk.Button(root, text="Save Tasks", command=save_tasks, width=20).pack(pady=5)
tk.Button(root, text="Load Tasks", command=load_tasks, width=20).pack(pady=5)

# Exit
tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=20)

root.mainloop()
