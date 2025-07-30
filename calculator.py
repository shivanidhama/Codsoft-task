import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter the valid numbers.")
    except ZeroDivisionError as zde:
        messagebox.showerror("Math Error", str(zde))

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x260")

# First number entry
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

# Second number entry
tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
tk.Label(root, text="Select operation:").pack(pady=5)
operation_var = tk.StringVar(value='+')
operation_menu = ttk.Combobox(root, textvariable=operation_var, values=['+', '-', '*', '/'], state="readonly")
operation_menu.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()


