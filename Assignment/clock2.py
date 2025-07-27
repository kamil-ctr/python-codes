import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")

clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
clock_label.pack(anchor="center", pady=20)

def update_time():
    current_time = time.strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

update_time()
root.mainloop()