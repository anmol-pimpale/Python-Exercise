# Create a base class named Employee as follows:
# Employee (
# -- class variables and methods
# 	organisation_name, 
# 	get_organisation_name(),
# 	set_organisation_name(org_name)

# -- instance variables and methods()
# emp_id,
# name,
# base_location,
# deployed_location,
# designation,
# salary ,
# get_employee_details() 	



# Create a subclass of Employee named Manager as follows:
# Manager(
	
# 	-- instance variables and methods()
# 	managed_employees[], # this is list of emp_references
# 	perform_appraisal_for_an_employee(emp_reference,percent_raise),
# 	get_manager_details()
# )

# Write a main method that does the following:
# create 3 objects of Employee 
# create an object of Manager_class and add the above 3 employee objects created as managed employees 
# display get_manager_details()
# for an employee do perform_appraisal_for_an_employee()


class Employee:
    organisation_name ="ABC corpuration"
    def __init__(self,emp_id,name,base_location,deployed_location,designation,salary):
        self.emp_id=emp_id
        self.name=name
        self.base_location=base_location
        self.deployed_location=deployed_location
        self.designation=designation
        self.salary=salary
    
    def get_organisation_name(cls):
        return cls.organisation_name
    
    def set_organisation_name(cls,org_name):
        cls.organisation_name = org_name
        
    def get_employee_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Base Location: {self.base_location}, Deployed Location: {self.deployed_location}, Designation: {self.designation}, Salary: {self.salary}"
    

