import tkinter as tk
from tkinter import messagebox
import json
import os

window = tk.Tk()
window.title("To-Do List")
window.geometry("450x600")
window.resizable(False, False)
window.configure(bg= "light grey")

tasks = []
FILE_NAME = "tasks.json"

def update_count():
    remaining = 0

    for task in tasks:
        if not task["status"].get():
            remaining += 1

    if remaining == 1:
        task_count.config(text="1 task remaining")
    else:
        task_count.config(text=f"{remaining} tasks remaining")

def save_tasks():
    data = []

    for task in tasks:
        data.append({
            "text": task["text"],
            "completed": task["status"].get()
        })

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_task():
    text = task_entry.get().strip()

    if text == "":
        messagebox.showwarning("Warning","Please enter a task.")
        return

    create_task(text, False)

    task_entry.delete(0, tk.END)

    update_count()
    save_tasks()

def create_task(text, completed=False):

    status = tk.BooleanVar(value=completed)

    task_box = tk.Frame(
        task_frame,
        relief="solid",
        borderwidth=1
    )

    task_box.pack(
        fill="x",
        padx=8,
        pady=4
    )

    checkbox = tk.Checkbutton(
        task_box,
        text=text,
        variable=status,
        font=("Arial", 11),
        anchor="w",
        padx= 4,
        pady= 3,
        command=task_changed
    )

    checkbox.pack(
        side="left",
        fill="x",
        expand=True,
        padx=5
    )

    delete_button = tk.Button(
        task_box,
        text="X",
        width=3,
        bg='red',
        fg='white',
        border= 2,
        command=lambda: delete_task(task_box)
    )

    delete_button.pack(
        side="right",
        padx=5
    )

    task = {
        "frame": task_box,
        "checkbox": checkbox,
        "status": status,
        "text": text
    }

    tasks.append(task)

def task_changed():
    update_count()
    save_tasks()

def delete_task(task_box):

    for task in tasks:

        if task["frame"] == task_box:

            task["frame"].destroy()
            tasks.remove(task)

            break

    update_count()
    save_tasks()

def clear_completed():

    for task in tasks[:]:

        if task["status"].get():

            task["frame"].destroy()
            tasks.remove(task)

    update_count()
    save_tasks()

def clear_all():

    if len(tasks) == 0:
        return

    answer = messagebox.askyesno("Clear All","Are you sure you want to delete all tasks?")
    if answer:

        for task in tasks:
            task["frame"].destroy()

        tasks.clear()

        update_count()
        save_tasks()

def load_tasks():

    if not os.path.exists(FILE_NAME):
        return

    try:

        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        for item in data:
            create_task(
                item["text"],
                item["completed"]
            )

    except:
        pass

title = tk.Label(
    window,
    text="TO-DO LIST",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)

task_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 12)
)

task_entry.pack(pady=5)

add_button = tk.Button(
    window,
    text="ADD TASK", 
    bg="white",
    fg="black",
    width=18,
    command=add_task
)

add_button.pack(pady=10)

task_frame = tk.Frame(
    window,
    width=390,
    height=300,
    relief="groove", bg ="white",
    borderwidth=2
)

task_frame.pack(
    pady=15,
    padx=20,
    fill="both",
    expand=False
)

task_count = tk.Label(
    window,
    text="0 tasks remaining",
    font=("Arial", 11)
)

task_count.pack(pady=5)

completed_button = tk.Button(
    window,
    text="CLEAR COMPLETED", 
    width=18,
    command=clear_completed
)

completed_button.pack(pady=5)

clear_button = tk.Button(
    window,
    text="CLEAR ALL",
    width=18,
    command=clear_all
)

clear_button.pack(pady=5)

load_tasks()

update_count()

window.mainloop()