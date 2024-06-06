# 4)Create the following program named "my_exception_store" with the menu below :

# Welcome User , What would you like to do today ?
#     1) Create a postive numbered list 
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list 
#     2) Create a negative  numbered list 
#     Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
#     3) Create a heterogenous list 
#     Note : raise an exception if the users creates a homogenous list (all elements of same datatype)

#     4) Refresh the program to start with blank lists
#     5) Exit

# Handle exceptions in the script for all operations 
# and let the user continue till he chooses to exit from the program 


class PositiveNumberException(Exception):
    pass

class NegativeNumberException(Exception):
    pass

class HeterogeneusException(Exception):
    pass

def create_positive_number_list(my_list):
    try:
        elements = int(input("Enter the number of elements in the positive number list: "))
        if elements <= 0:
            raise PositiveNumberException("Number of elements cannot be zero or negative.")
        for i in range(elements):
            num = int(input(f"Enter element {i+1}: "))
            if num <= 0:
                raise PositiveNumberException("All elements must be positive numbers.")
            my_list.append(num)
    except PositiveNumberException:
        print("Invalid input. Please enter a positive integer.")

def create_negative_number_list(my_list):
    try:
        elements = int(input("Enter the number of elements in the negative number list: "))
        if elements >= 0:
            raise NegativeNumberException("Number of elements cannot be positive or zero.")
        for i in range(elements):
            num = int(input(f"Enter element {i+1}: "))
            if num >= 0:
                raise NegativeNumberException("All elements must be negative numbers.")
            my_list.append(num)
    except NegativeNumberException:
        print("Invalid input. Please enter a negative integer.")
        
def create_heterogeneous_list(my_list):
    try:
        num_elements = int(input("Enter the number of elements in the heterogeneous list: "))
        if num_elements <= 0:
            raise HeterogeneusException("Number of elements cannot be zero or negative.")
        for i in range(num_elements):
            element = input(f"Enter element {i+1}: ")
            if isinstance(my_list, list) and all(isinstance(item, type(element)) for item in my_list):
                raise HeterogeneusException("List cannot be homogeneous.")
            my_list.append(element)
    except HeterogeneusException:
        print("Invalid input. Please enter a valid value.")
    
        

def my_exception_store():
    list_positive = []
    list_negative = []
    list_heterogeneus =[]

    while True:
        try:
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) Refresh the program to start with blank lists")
            print("4) Exit  ")

            choice = int(input("Please enter your choice !!!! "))
            if choice == 1:
                create_positive_number_list(list_positive)
            elif choice == 2:
                create_negative_number_list(list_negative)
            elif choice ==3:
                create_heterogeneous_list(list_heterogeneus)
            elif choice == 4:
                list_positive.clear()
                list_negative.clear()
                print("Store restarted !!!! ")
            elif choice == 5:
                break
            else:
                print("Please choose something from the above")
        except Exception:
            print("An error occur")

my_exception_store()