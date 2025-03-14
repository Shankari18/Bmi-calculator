import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

def calculate_bmi_gui():
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if age <= 0:
            messagebox.showerror("Error", "Age must be a positive number.")
            return
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive numbers.")
            return

        bmi, category = calculate_bmi(weight, height)
        result_label.config(text=f"Age: {age}\nYour BMI: {bmi:.2f}\nCategory: {category}", fg="black", bg="#BBDEFB", font=("Times Roman", 12), padx=10, pady=10)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")
root.configure(bg="#BBDEFB")

header_label = tk.Label(root, text="BMI Calculator", font=("Times Roman", 16, "bold"), bg="#BBDEFB", fg="white", pady=10)
header_label.grid(row=0, column=0, columnspan=2, pady=10)

fields = ["Enter Age:", "Enter Weight (kg):", "Enter Height (m):"]
entries = []

for i, field in enumerate(fields):
    tk.Label(root, text=field, bg="#BBDEFB", fg="black", font=("Times Roman", 12), anchor="w").grid(row=i + 1, column=0, padx=20, pady=5, sticky="w")
    entry = tk.Entry(root, bg="#e0e0e0", fg="black", font=("Times Roman", 12), width=15)
    entry.grid(row=i + 1, column=1, padx=20, pady=5)
    entries.append(entry)

age_entry, weight_entry, height_entry = entries

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi_gui, bg="#4CAF50", fg="white", font=("Times Roman", 12, "bold"), padx=10, pady=5)
calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="", font=("Times Roman", 12), bg="#BBDEFB", fg="black", pady=20)
result_label.grid(row=5, column=0, columnspan=2, sticky="nsew")

root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
