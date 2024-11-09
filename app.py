# app.py
import tkinter as tk
from tkinter import messagebox
from crud_operations import create_employee, read_employees, update_employee, delete_employee
from database import create_table

# Initialize the database table
create_table()

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("500x400")

        # Form Labels and Entries
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(root, text="Department:").grid(row=2, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(root)
        self.age_entry = tk.Entry(root)
        self.department_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)
        self.age_entry.grid(row=1, column=1)
        self.department_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="Add Employee", command=self.add_employee).grid(row=3, column=0, pady=10)
        tk.Button(root, text="View Employees", command=self.view_employees).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Update Employee", command=self.update_employee).grid(row=4, column=0, pady=10)
        tk.Button(root, text="Delete Employee", command=self.delete_employee).grid(row=4, column=1, pady=10)

        # Output Box
        self.output_box = tk.Text(root, height=10, width=50)
        self.output_box.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_employee(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        department = self.department_entry.get()
        result = create_employee(name, age, department)
        messagebox.showinfo("Info", result)
        self.clear_entries()

    def view_employees(self):
        employees = read_employees()
        self.output_box.delete("1.0", tk.END)
        for emp in employees:
            self.output_box.insert(tk.END, f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}\n")

    def update_employee(self):
        emp_id = int(self.name_entry.get())
        name = self.age_entry.get() or None
        age = int(self.department_entry.get()) if self.department_entry.get() else None
        department = self.department_entry.get() or None
        result = update_employee(emp_id, name=name, age=age, department=department)
        messagebox.showinfo("Info", result)
        self.clear_entries()

    def delete_employee(self):
        emp_id = int(self.name_entry.get())
        result = delete_employee(emp_id)
        messagebox.showinfo("Info", result)
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()
