import tkinter as tk
from tkinter import messagebox

# add task to list
def add_task():
    task = entry.get()
    priority_level = priority.get()  # get selected priority
    if task:
        # frame for task, checkbox, and priority label
        task_frame = tk.Frame(task_list_frame)
        task_frame.pack(fill=tk.X, pady=2)

        # checkbox for task completion
        completed_var = tk.BooleanVar()
        completed_check = tk.Checkbutton(task_frame, variable=completed_var, command=lambda: mark_completed(task_frame, completed_var))
        completed_check.pack(side=tk.LEFT, padx=5)

        # label for task text
        task_label = tk.Label(task_frame, text=task, width=40, anchor="w")
        task_label.pack(side=tk.LEFT, padx=5)

        # label for priority (color-coded)
        priority_label = tk.Label(task_frame, text="    ", bg=get_priority_color(priority_level))
        priority_label.pack(side=tk.RIGHT, padx=5)

        # Store task details in dictionary
        task_data = {
            "frame": task_frame,
            "completed_var": completed_var,
            "task_label": task_label,
            "priority_label": priority_label
        }
        tasks.append(task_data)

        # Clear entry widget
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# delete selected task
def delete_task():
    if tasks:
        for task_data in tasks:
            if task_data["completed_var"].get():  # Check if task is marked as completed
                task_data["frame"].destroy()  # Remove task frame from the GUI
                tasks.remove(task_data)  # Remove task from list
                break
        else:
            messagebox.showwarning("Warning", "No completed task selected.")
    else:
        messagebox.showwarning("Warning", "No tasks to delete.")

# mark task as completed (appearance)
def mark_completed(task_frame, completed_var):
    for widget in task_frame.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") != "    ":
            if completed_var.get():
                widget.config(fg="gray", font=("Arial", 10, "overstrike"))
            else:
                widget.config(fg="black", font=("Arial", 10))

# get color for priority label
def get_priority_color(priority_level):
    if priority_level == "High":
        return "red"
    elif priority_level == "Medium":
        return "yellow"
    else:
        return "green"

# main window
root = tk.Tk()
root.title("To-Do List")

# frame for entry and buttons
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# entry widget for adding tasks
entry = tk.Entry(input_frame, width=40)
entry.grid(row=0, column=0, padx=5)

# button to add tasks
add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5)

# frame to hold list of tasks
task_list_frame = tk.Frame(root)
task_list_frame.pack(pady=10)

# frame for radio buttons (priority selection)
priority_frame = tk.Frame(root)
priority_frame.pack(pady=10)

# radio buttons for task priority
priority = tk.StringVar()
priority.set("Low")

low_priority = tk.Radiobutton(priority_frame, text="Low Priority", variable=priority, value="Low")
low_priority.grid(row=0, column=0, padx=5)

medium_priority = tk.Radiobutton(priority_frame, text="Medium Priority", variable=priority, value="Medium")
medium_priority.grid(row=0, column=1, padx=5)

high_priority = tk.Radiobutton(priority_frame, text="High Priority", variable=priority, value="High")
high_priority.grid(row=0, column=2, padx=5)

# button to delete completed tasks
delete_button = tk.Button(root, text="Delete Completed Task", command=delete_task)
delete_button.pack(pady=10)

# List to store all tasks
tasks = []

# Run application loop
root.mainloop()
