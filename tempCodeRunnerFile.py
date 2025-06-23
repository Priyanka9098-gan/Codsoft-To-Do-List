import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Cloud To Do List")
root.attributes("-fullscreen", True)

# Screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load background image
bg_image = Image.open("op.jpg")
bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
root.bg_photo = bg_photo

# Load pink cloud panel
cloud_img = Image.open("tp.jpg")
cloud_w, cloud_h = 500, 550
cloud_img = cloud_img.resize((cloud_w, cloud_h), Image.LANCZOS)
cloud_photo = ImageTk.PhotoImage(cloud_img)

note_x = (screen_width - cloud_w) // 2
note_y = (screen_height - cloud_h) // 2

cloud_label = tk.Label(root, image=cloud_photo, bd=0)
cloud_label.image = cloud_photo
cloud_label.place(x=note_x, y=note_y)

# Fonts and styling
FONT = ("Segoe UI", 13)
TITLE_FONT = ("Georgia", 22, "bold")
PINK_MATCH = "#f78bb4"
BUTTON_BG = "#f78bb4"
BUTTON_HOVER = "#e75480"

# Title
title_label = tk.Label(root, text="To Do List", font=TITLE_FONT, bg=PINK_MATCH, fg="#060a0e")
title_label.place(x=note_x + 170, y=note_y + 40)

# Task list
task_listbox = tk.Listbox(
    root, font=FONT, bg=PINK_MATCH, fg="#0b0c0d", bd=0,
    selectbackground="#ffc0cb", highlightthickness=0, relief="flat"
)
task_listbox.place(x=note_x + 60, y=note_y + 90, width=380, height=200)

# Seamless entry field
task_entry = tk.Entry(
    root, font=FONT, bg=PINK_MATCH, fg="#090a0a",
    bd=0, highlightthickness=0, relief="flat", insertbackground="#0c0d0e"
)
task_entry.place(x=note_x + 60, y=note_y + 310, width=250, height=28)

# Functions
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

# Buttons
add_button = tk.Button(root, text="Add", font=FONT, bg=BUTTON_BG, fg="white", bd=0, padx=10, pady=2, command=add_task)
add_button.place(x=note_x + 320, y=note_y + 310)

delete_button = tk.Button(root, text="Delete", font=FONT, bg=BUTTON_BG, fg="white", bd=0, padx=10, pady=2, command=delete_task)
delete_button.place(x=note_x + 180, y=note_y + 360)

# Hover effects
def on_enter(e): e.widget.config(bg=BUTTON_HOVER)
def on_leave(e): e.widget.config(bg=BUTTON_BG)

for btn in (add_button, delete_button):
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Exit with Escape key
root.bind("<Escape>", lambda e: root.destroy())
root.mainloop()