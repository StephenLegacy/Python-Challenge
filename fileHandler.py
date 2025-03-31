import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os

# Function to create input.txt and allow editing
def create_default_file():
    if not os.path.exists("input.txt"):  # Check if input.txt exists
        with open("input.txt", "w") as f:
            f.write("This is a sample text file.\nIt contains multiple lines.\nPython is amazing!\nFile handling is fun.\nLet's process this file.")
    open_file("input.txt")

# Function to open a file and allow editing
def open_file(filename=None):
    if filename is None:
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filename:
            return
    
    text_area.delete(1.0, tk.END)  # Clear previous text
    with open(filename, "r") as file:
        text_area.insert(tk.END, file.read())
    root.title(f"Editing - {os.path.basename(filename)}")
    save_button.config(state=tk.NORMAL)  # Enable saving
    process_button.config(state=tk.NORMAL)
    global current_file
    current_file = filename

# Function to save the edited file
def save_file():
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Success", f"File '{current_file}' saved successfully!")

# Function to process the text file
def process_file():
    if not current_file:
        messagebox.showwarning("Warning", "No file opened to process!")
        return
    
    with open(current_file, "r") as file:
        content = file.read()
    word_count = len(content.split())
    uppercase_text = content.upper()
    
    output_file = "output.txt"
    with open(output_file, "w") as file:
        file.write(uppercase_text + f"\n\nWord Count: {word_count}")
    
    messagebox.showinfo("Success", f"Processed file saved as '{output_file}' with word count: {word_count}")
    open_file(output_file)  # Open processed file for review

# Function to exit the application
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to quit?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Text File Processor")
root.geometry("600x500")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

current_file = None  # Track the currently opened file

frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10, relief=tk.RAISED, bd=5)
frame.pack(pady=10)

text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=15, font=("Arial", 12), bd=2, relief=tk.GROOVE)
text_area.pack()

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

create_button = tk.Button(button_frame, text="Create Input File", command=create_default_file, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, relief=tk.GROOVE)
create_button.grid(row=0, column=0, padx=5)

open_button = tk.Button(button_frame, text="Open File", command=open_file, bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, relief=tk.GROOVE)
open_button.grid(row=0, column=1, padx=5)

save_button = tk.Button(button_frame, text="Save File", command=save_file, bg="#FF9800", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, relief=tk.GROOVE, state=tk.DISABLED)
save_button.grid(row=0, column=2, padx=5)

process_button = tk.Button(button_frame, text="Process File", command=process_file, bg="#9C27B0", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, relief=tk.GROOVE, state=tk.DISABLED)
process_button.grid(row=0, column=3, padx=5)

exit_button = tk.Button(root, text="Exit", command=exit_app, bg="#F44336", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, relief=tk.GROOVE)
exit_button.pack(pady=5)

create_default_file()  # Start with input.txt
root.mainloop()
