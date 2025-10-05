# Employee Directory Program – Review Classes/Objects, Files Read/Write and Dictionaries
# Name: Aaron Moreno
# Date: 10/05/2025
# Description:
# This program manages a company’s employee directory. It reads employee data from a file,
# allows adding and deleting employees, converts the data into a dictionary,
# and writes updates back to the file.

# --------------------------------------------
# Employee Class
# --------------------------------------------
class Employee:
    """Employee class to keep track of employee info"""

    def __init__(self, ID=-999, name='', department='', pay=0.0):
        self.set_ID(ID)
        self.set_name(name)
        self.set_department(department)
        self.set_pay(pay)

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_pay(self):
        return self.pay

    def set_pay(self, pay):
        self.pay = pay

    def __str__(self):
        return f"{self.get_ID()} {self.get_name()} {self.get_department()} {self.get_pay()}"


# --------------------------------------------
# Employee Directory Class
# --------------------------------------------
class EmployeeDirectory:
    """Track employee info in the directory"""

    def __init__(self):
        self.employee_list = []
        self.employee_dict = {}

    def add_employee(self, employee):
        """Add employee only if ID not already in list"""
        if not any(emp.get_ID() == employee.get_ID() for emp in self.employee_list):
            self.employee_list.append(employee)

    def del_employee(self, employee):
        """Delete employee by ID"""
        for emp in self.employee_list:
            if emp.get_ID() == employee.get_ID():
                self.employee_list.remove(emp)
                return
        print(f"ID:{employee.get_ID()} does not exist, deletion is aborted")

    def read_file(self, file_name):
        """Read employees.txt file and return a list of Employee objects"""
        employees = []
        try:
            with open(file_name, "r") as f:
                for line in f:
                    parts = line.strip().split()
                    if len(parts) == 4:
                        ID = int(parts[0])
                        name = parts[1]
                        department = parts[2]
                        pay = float(parts[3])
                        employees.append(Employee(ID, name, department, pay))
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Starting with empty list.")
        return employees

    def update_employee_dir(self, file_name):
        """Read file and remove duplicates automatically"""
        employees = self.read_file(file_name)
        unique_ids = set()
        self.employee_list = []
        for emp in employees:
            if emp.get_ID() not in unique_ids:
                self.employee_list.append(emp)
                unique_ids.add(emp.get_ID())

    def write_to_file(self, file_name):
        """Write the updated employee list back to file"""
        with open(file_name, "w") as f:
            for emp in self.employee_list:
                f.write(str(emp) + "\n")

    def write_to_dict(self):
        """Convert the employee list to a dictionary"""
        self.employee_dict = {'ID': [], 'name': [], 'department': [], 'pay': []}
        for emp in self.employee_list:
            self.employee_dict['ID'].append(emp.get_ID())
            self.employee_dict['name'].append(emp.get_name())
            self.employee_dict['department'].append(emp.get_department())
            self.employee_dict['pay'].append(emp.get_pay())

    def display_dict(self):
        """Display the employee dictionary in assignment format"""
        print("--- Employee Directory Output ---")
        for key, value in self.employee_dict.items():
            print(f"{key} : {value}")
        print("--------------------------------")


# --------------------------------------------
# Test Program (Main Section)
# --------------------------------------------
if __name__ == "__main__":
    try:
        emp_dir = EmployeeDirectory()
        emp_dir.update_employee_dir("employees.txt")

        # Create new employees
        emp1 = Employee(106, 'Emp1', 'Accounting', 56000.0)
        emp2 = Employee(107, 'Emp2', 'Sales', 80000.0)
        emp3 = Employee(108, 'Emp3', 'Marketing', 90000.0)

        # Add emp1 and emp2 safely (duplicates prevented)
        emp_dir.add_employee(emp1)
        emp_dir.add_employee(emp2)

        # Attempt to delete emp3 (not in list)
        emp_dir.del_employee(emp3)

    except Exception as ex:
        print("Error:", ex)
    finally:
        # Save updated list to file
        emp_dir.write_to_file("employees.txt")

        # Convert list to dictionary
        emp_dir.write_to_dict()

        # Display dictionary
        emp_dir.display_dict()