 #Define a variable named "raise_salary_percentage" and get the salary raise 
#percentage from the user, Now apply the raise to an employee
#with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
#print the incremented salary to the console

raise_salary_percentage = float(input("Enter the salary raise percentage: "))

existing_salary = 900
incremented_salary = existing_salary * (1 + raise_salary_percentage / 100)
print("The incremented salary for gaurav is: ", incremented_salary)
