import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showwarning("Warning", "Length must be greater than 0!")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number!")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Label
tk.Label(root, text="Enter Password Length:").pack(pady=10)

# Entry field
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display Password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, state='readonly', width=30)
password_entry.pack(pady=10)

# Run the application
root.mainloop()
