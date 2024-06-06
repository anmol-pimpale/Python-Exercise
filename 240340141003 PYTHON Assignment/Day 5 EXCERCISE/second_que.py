
# Exercise 2.1 : Create a dictionary like this by taking values from the user:
# here the idea is to support a generic dictionary where the values could be of any datatype
# and the keys are strings


employee_dict = {}


employee_dict['employee_id'] = int(input("Enter employee ID: "))
employee_dict['employee_name'] = input("Enter employee name: ")
employee_dict['account_number'] = int(input("Enter account number: "))
employee_dict['salary'] = float(input("Enter salary: "))

address = {}
address['home_address'] = input("Enter home address: ")
address['work_address'] = input("Enter work address: ")
employee_dict['address'] = address

awards = input("Enter awards (comma separated): ").split(',')
employee_dict['awards'] = [award.strip() for award in awards]

subjects = input("Enter subjects enrolled (comma separated): ").split(',')
employee_dict['subjects_enrolled'] = tuple(subject.strip() for subject in subjects)


print(employee_dict)