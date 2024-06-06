
from first_ques import Employee
class Manager(Employee):
    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary, managed_employees=None):
        super().__init__(emp_id, name, base_location, deployed_location, designation, salary)
        if managed_employees is None:
            self.managed_employees=[]
        else:
            self.managed_employee=managed_employees
    
    
    def perform_appraisal_for_an_employee(self,emp_reference,percent_raise):
        
        for employee in self.managed_employee:
            if employee == emp_reference:
                employee.salary += employee.salary * (percent_raise /100)
                return f"Appraisal performed for {employee.name} with {percent_raise}% raise. New salary: {employee.salary}"
        return "Employee not found."

    def get_manager_details(self):
        return f"Manager ID:{self.emp_id},Name:{self.name},Base location:{self.base_location},deployed location:{self.deployed_location},designation:{self.designation},salary:{self.salary}"
    
def main():
    print("i am in main function")
    emp1 = Employee(1, "jeet", "India", "Chicago", "HPC Engineer", 80000)
    emp2 = Employee(2, "sheekha", "India", "San Francisco", "Project Manager", 90000)
    emp3 = Employee(3, "sonali", "India", "Denver", "Data Analyst", 70000)
    emp4 = Employee(4,"sagar","India","Dubai","Senior Devloper",100000)

    manager = Manager(100, "jeet", "India", "Chicago", "HPC Engineer", 120000, [emp1, emp2, emp3])

    print(manager.get_manager_details())
    print(manager.perform_appraisal_for_an_employee(emp1, 3))
    print(manager.get_manager_details())


main()
          