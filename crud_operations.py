# crud_operations.py
from database import connect


def create_employee(name, age, department):
    """Inserts a new employee record."""
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)", (name, age, department))
        connection.commit()
        cursor.close()
        connection.close()
        return "Employee added successfully"
    return "Failed to add employee"


def read_employees():
    """Fetches all employee records."""
    connection = connect()
    employees = []
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        cursor.close()
        connection.close()
    return employees


def update_employee(employee_id, name=None, age=None, department=None):
    """Updates an employee's details."""
    connection = connect()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE employees SET "
        fields = []
        if name:
            fields.append("name = %s")
        if age:
            fields.append("age = %s")
        if department:
            fields.append("department = %s")

        query += ", ".join(fields) + " WHERE id = %s"
        values = tuple([x for x in (name, age, department) if x is not None] + [employee_id])

        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return f"Employee ID {employee_id} updated successfully"
    return "Failed to update employee"


def delete_employee(employee_id):
    """Deletes an employee record."""
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return f"Employee ID {employee_id} deleted successfully"
    return "Failed to delete employee"
