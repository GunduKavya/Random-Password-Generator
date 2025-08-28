import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("No character sets selected.")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

import tkinter as tk
from tkinter import messagebox
import pyperclip
from password_generator import generate_password

def generate():
    try:
        length = int(length_entry.get())
        password = generate_password(
            length=length,
            use_upper=upper_var.get(),
            use_lower=lower_var.get(),
            use_digits=digits_var.get(),
            use_symbols=symbols_var.get()
        )
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    pyperclip.copy(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Advanced Password Generator")

# Length input
tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1)

# Character set options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).grid(row=1, column=0, sticky='w')
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).grid(row=2, column=0, sticky='w')
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=3, column=0, sticky='w')
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=4, column=0, sticky='w')

# Generate button
tk.Button(root, text="Generate Password", command=generate).grid(row=5, column=0, columnspan=2)

# Result field
result_entry = tk.Entry(root, width=40)
result_entry.grid(row=6, column=0, columnspan=2)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=7, column=0, columnspan=2)

root.mainloop()
