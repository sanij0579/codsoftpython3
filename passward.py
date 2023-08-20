import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    name = name_entry.get()
    password_length = int(length_entry.get())
    if password_length < 6:
        messagebox.showerror("Invalid Length", "Password length should be at least 6 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))

    # Include the user's name in the password
    if name:
        password = name + '_' + password

    password_display.config(text="Generated Password: " + password)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
name_label = tk.Label(root, text="Enter Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_display = tk.Label(root, text="Generated Password: ")
password_display.pack()

# Run the main event loop
root.mainloop()

