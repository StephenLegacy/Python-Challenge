import tkinter as tk
from tkinter import messagebox
import pygame
import threading
import time

# Initialize pygame for audio feedback
pygame.mixer.init()

def play_sound():
    try:
        sound = pygame.mixer.Sound("alert.wav")  # Ensure you have an alert.wav file in the same directory
        sound.play()
        time.sleep(30)  # Allow sound to play for 30 seconds
        sound.stop()
    except pygame.error:
        messagebox.showwarning("Audio Error", "Unable to play sound. Check the file format.")

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

def calculate_and_display():
    try:
        price = float(price_entry.get())  # Get the entered price and convert to float
        discount = float(discount_entry.get())  # Get the discount percentage and convert to float
        final_price = calculate_discount(price, discount)  # Calculate the final price
        threading.Thread(target=play_sound).start()  # Play alert sound in a separate thread
        messagebox.showinfo("Final Price", f"Final price after discount: ${final_price:.2f}")  # Display the final price
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers for price and discount.")  # Show error for invalid input

# Create the main application window
app = tk.Tk()
app.title("Discount Calculator")  # Set window title
app.geometry("500x400")  # Set window size
app.configure(bg="#1e1e2d")  # Set background color

# Label and input field for original price
label1 = tk.Label(app, text="Original Price:", fg="white", bg="#1e1e2d", font=("Arial", 14))
label1.pack(pady=10)
price_entry = tk.Entry(app, font=("Arial", 14))
price_entry.pack()

# Label and input field for discount percentage
label2 = tk.Label(app, text="Discount Percentage:", fg="white", bg="#1e1e2d", font=("Arial", 14))
label2.pack(pady=10)
discount_entry = tk.Entry(app, font=("Arial", 14))
discount_entry.pack()

# Button to calculate discount
calculate_button = tk.Button(app, text="Calculate", command=calculate_and_display, font=("Arial", 14), bg="#e74c3c", fg="white", padx=15, pady=5)
calculate_button.pack(pady=20)

# Button to close the application
close_button = tk.Button(app, text="Exit", command=app.quit, font=("Arial", 14), bg="#d35400", fg="white", padx=15, pady=5)
close_button.pack(pady=10)

# Run the main event loop
app.mainloop()
