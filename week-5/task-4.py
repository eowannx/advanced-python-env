class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):
        return self.__salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus

def display_employees(employees):
    for emp in employees:
        print(f"Role: {emp.get_role()}, Name: {emp.name}, Salary: {emp.get_salary()}")

def main():
    emp1 = Employee("Alice", 50000)
    mgr1 = Manager("Bob", 80000, 15000)
    
    employee_list = [emp1, mgr1]
    display_employees(employee_list)

if __name__ == "__main__":
    main()