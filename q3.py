# Creating Employee class
class Employee:
    def __init__(self, name,employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated Salary for {self.name}: ${self.salary}")


# Creating a department class to manage employees
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def display_employees(self):
        print(f"Employees in {self.department_name} Department:")
        for emp in self.employees:
            emp.display_info()

    def claculate_total_salary(self):
        total_salary = sum(emp.salary for emp in self.employees)
        print(f"Total salary for {self.department_name} Department: ${total_salary}")



# creating instances
if __name__ == "__main__":

    emp1 = Employee("Tommy", "201", 60000)
    emp2 = Employee("Ezy", "202", 70000)

    hr_department = Department("HR")
    hr_department.add_employee(emp1)
    hr_department.add_employee(emp2)

    hr_department.display_employees()
    hr_department.claculate_total_salary()

    emp1.update_salary(65000)
    hr_department.claculate_total_salary()  