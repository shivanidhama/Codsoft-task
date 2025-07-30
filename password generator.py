import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length_str = length_entry.get()

    if not length_str.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    length = int(length_str)
    if length < 1:
        messagebox.showerror("Invalid Length", "Password length must be at least 1.")
        return

    # Build character set based on user choices
    char_set = ""
    if var_lower.get():
        char_set += string.ascii_lowercase
    if var_upper.get():
        char_set += string.ascii_uppercase
    if var_digit.get():
        char_set += string.digits
    if var_symbol.get():
        char_set += string.punctuation

    if not char_set:
        messagebox.showwarning("No Option Selected", "Please select at least one character type.")
        return

    # Generate password
    password = ''.join(random.choice(char_set) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pwd = password_entry.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Custom Password Generator")
root.geometry("450x400")
root.config(bg="#f5faff")

tk.Label(root, text="Custom Password Generator", font=("Arial", 16, "bold"), bg="#f5faff").pack(pady=10)

# Password Length
tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#f5faff").pack()
length_entry = tk.Entry(root, width=10, font=("Arial", 12), justify='center')
length_entry.pack(pady=5)

# Checkboxes for character types
tk.Label(root, text="Include Character Types:", font=("Arial", 12, "bold"), bg="#f5faff").pack(pady=10)

var_lower = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_digit = tk.BooleanVar(value=True)
var_symbol = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Lowercase (a-z)", variable=var_lower, font=("Arial", 11), bg="#f5faff").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Uppercase (A-Z)", variable=var_upper, font=("Arial", 11), bg="#f5faff").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Digits (0-9)", variable=var_digit, font=("Arial", 11), bg="#f5faff").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Symbols (!@#$)", variable=var_symbol, font=("Arial", 11), bg="#f5faff").pack(anchor='w', padx=40)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12)).pack(pady=15)

# Password Output
tk.Label(root, text="Generated Password:", font=("Arial", 12), bg="#f5faff").pack()
password_entry = tk.Entry(root, width=30, font=("Arial", 12), justify='center')
password_entry.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12)).pack(pady=10)

root.mainloop()
