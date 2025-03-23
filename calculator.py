import tkinter as tk
from tkinter import ttk

# Evaluate the expression
def calculate():
    try:
        result.set(eval(expression.get()))
    except Exception:
        result.set("Error")

# Add characters to the expression for calculator
def press(key):
    expression.set(expression.get() + str(key))

# Clear the entire input
def clear():
    expression.set("")
    result.set("")

# Delete the last character
def delete():
    expression.set(expression.get()[:-1])

# Main window setup
root = tk.Tk()
root.title(" Python  Calculator | STEPHEN OLOO ")
root.geometry("400x600")
root.config(bg="#1e1e1e")

expression = tk.StringVar()
result = tk.StringVar()

# Expression entry field
entry = ttk.Entry(root, textvariable=expression, font=('Arial', 28))
entry.pack(fill='both', padx=10, pady=20, ipady=10)

# Result display
result_label = ttk.Label(root, textvariable=result, font=('Arial', 24), background="#1e1e1e", foreground="#00FF00")
result_label.pack(fill='both', padx=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '⌫', '+'],
]

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# Create buttons dynamically
for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e1e1e")
    row_frame.pack(expand=True, fill='both')
    for btn in row:
        if btn == '⌫':
            action = delete
        else:
            action = lambda x=btn: press(x)
        tk.Button(row_frame, text=btn, font=('Arial', 20), command=action, bg="#333", fg="white", width=5, height=2).pack(side='left', expand=True, fill='both')

# Control buttons (Clear and Equal)
control_frame = tk.Frame(root, bg="#1e1e1e")
control_frame.pack(expand=True, fill='both', padx=10, pady=10)

tk.Button(control_frame, text='C', font=('Arial', 24), command=clear, bg="#ff4d4d", fg="white").pack(side='left', expand=True, fill='both', padx=5)
tk.Button(control_frame, text='=', font=('Arial', 24), command=calculate, bg="#00bfff", fg="white").pack(side='left', expand=True, fill='both', padx=5)

root.mainloop()
