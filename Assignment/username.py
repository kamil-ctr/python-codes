import tkinter as tk
from tkinter import messagebox

def submit():
    username = entry_username.get()
    password = entry_password.get()
    
    if username and password:
        messagebox.showinfo("Info", "Username and Password submitted!")
    else:
        messagebox.showwarning("Warning", "Please enter both username and password.")

root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

root.mainloop()