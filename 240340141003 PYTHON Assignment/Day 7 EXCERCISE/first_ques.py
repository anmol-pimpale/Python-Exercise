#Exercise 01 : Classes and objects -- try creating this in oops world
# main:

# 1) create an object employee(100,1000,1)  
# 2) do the following for the created object
# // direct access using .notation
# empid
# emp_salary
# mgr_id
# 3) print the department name 
# 4) display the expertise for the employees 
# 5) Deleting Attributes and Objects

class Employee:
    department_name = "CADC"  # class variable

    def __init__(self, emp_id, emp_salary, mgr_id):
        self.emp_id = emp_id
        self.emp_salary = emp_salary  # use public variable for simplicity
        self.mgr_id = mgr_id

    def get_emp_salary(self):
        return self.emp_salary

    def set_emp_salary(self, rcv_salary):
        if rcv_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.emp_salary = rcv_salary

    @classmethod
    def get_department_name(cls):
        return cls.department_name

    @staticmethod
    def field_expertise():
        return "All employees are experts in their respective fields."

def main():
    employee = Employee(100, 1000, 1)

    # direct access using.notation
    print(employee.emp_id)
    print(employee.get_emp_salary())
    print(employee.mgr_id)

    # print the department name
    print(Employee.get_department_name())

    # display the expertise for the employees
    print(Employee.field_expertise())

    # set the salary
    employee.set_emp_salary(1200)
    print(employee.get_emp_salary())

    # try to set a negative salary
    try:
        employee.set_emp_salary(-100)
    except ValueError:
        print("salary")

    # Deleting Attributes and Objects
    del employee.emp_id  # delete an attribute
    del employee  # delete the object

if __name__ == "__main__":
    main()