import tkinter as tk
from tkinter import ttk, messagebox

# ------------------ Classes (OOP Part) ------------------
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False

    def power_on(self):
        self.is_on = True
        return f"{self.model} is now ON 🔋"

    def power_off(self):
        self.is_on = False
        return f"{self.model} is now OFF 📴"

    def specs(self):
        return f"📱 {self.brand} {self.model} - {self.storage}GB"

class SmartPhonePro(Smartphone):
    def __init__(self, brand, model, storage, stylus_support):
        super().__init__(brand, model, storage)
        self.stylus_support = stylus_support

    def show_pro_features(self):
        return f"🆕 {self.model} Pro supports stylus: {self.stylus_support}"

class Vehicle:
    def move(self):
        return "The vehicle moves"

class Car(Vehicle):
    def move(self):
        return "🚗 The car drives on the road."

class Plane(Vehicle):
    def move(self):
        return "✈️ The plane flies in the sky."

class Boat(Vehicle):
    def move(self):
        return "🚢 The boat sails on the water."

# ------------------ GUI App ------------------
class MyWorldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌍 MyWorld Simulator")
        self.root.geometry("500x400")

        title = tk.Label(root, text="🌍 MyWorld Simulator", font=("Arial", 20))
        title.pack(pady=20)

        # Buttons to navigate
        tk.Button(root, text="📱 Smartphone Simulator", width=25, command=self.open_smartphone_window).pack(pady=10)
        tk.Button(root, text="🚗 Vehicle Movement Simulator", width=25, command=self.open_vehicle_window).pack(pady=10)
        tk.Button(root, text="❌ Exit", width=25, command=root.quit).pack(pady=10)

    # Smartphone Window
    def open_smartphone_window(self):
        win = tk.Toplevel(self.root)
        win.title("📱 Smartphone Creator")
        win.geometry("450x450")

        tk.Label(win, text="Smartphone Creator", font=("Arial", 16)).pack(pady=10)

        # Entry fields
        brand_var = tk.StringVar()
        model_var = tk.StringVar()
        storage_var = tk.StringVar()
        pro_var = tk.StringVar(value="no")
        stylus_var = tk.StringVar(value="no")

        tk.Label(win, text="Brand").pack()
        tk.Entry(win, textvariable=brand_var).pack()

        tk.Label(win, text="Model").pack()
        tk.Entry(win, textvariable=model_var).pack()

        tk.Label(win, text="Storage (GB)").pack()
        tk.Entry(win, textvariable=storage_var).pack()

        tk.Label(win, text="Pro Version? (yes/no)").pack()
        tk.Entry(win, textvariable=pro_var).pack()

        tk.Label(win, text="Stylus Support? (yes/no)").pack()
        tk.Entry(win, textvariable=stylus_var).pack()

        output_label = tk.Label(win, text="", fg="green", wraplength=400, justify="left")
        output_label.pack(pady=10)

        def simulate_phone():
            brand = brand_var.get()
            model = model_var.get()
            storage = storage_var.get()
            is_pro = pro_var.get().lower() == "yes"

            if is_pro:
                stylus = stylus_var.get()
                phone = SmartPhonePro(brand, model, storage, stylus)
                result = (
                    phone.specs() + "\n" +
                    phone.power_on() + "\n" +
                    phone.show_pro_features() + "\n" +
                    phone.power_off()
                )
            else:
                phone = Smartphone(brand, model, storage)
                result = (
                    phone.specs() + "\n" +
                    phone.power_on() + "\n" +
                    phone.power_off()
                )
            output_label.config(text=result)

        tk.Button(win, text="Simulate Smartphone", command=simulate_phone).pack(pady=10)

    # Vehicle Window
    def open_vehicle_window(self):
        win = tk.Toplevel(self.root)
        win.title("🚗 Vehicle Movement Simulator")
        win.geometry("400x300")

        tk.Label(win, text="Choose Vehicle", font=("Arial", 16)).pack(pady=10)

        vehicle_var = tk.StringVar(value="Car")
        vehicle_options = ["Car", "Plane", "Boat"]

        dropdown = ttk.Combobox(win, textvariable=vehicle_var, values=vehicle_options, state="readonly")
        dropdown.pack(pady=10)

        output_label = tk.Label(win, text="", font=("Arial", 12), fg="blue")
        output_label.pack(pady=20)

        def simulate_movement():
            choice = vehicle_var.get()
            if choice == "Car":
                v = Car()
            elif choice == "Plane":
                v = Plane()
            else:
                v = Boat()

            output_label.config(text=v.move())

        tk.Button(win, text="Move Vehicle", command=simulate_movement).pack(pady=10)

# ------------------ Run App ------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MyWorldApp(root)
    root.mainloop()
