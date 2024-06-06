# 1) Create a program named "my_dict_store" which support following operations on 
# dictionary named "capitals" which would have keys as their country and values as their capitals
# respectively from the user
# for ex: "India" : "New Delhi" ,"USA" : "Washington DC","Nepal": "Kathmandu","Ukraine" : "Kyiv"
# is provided by the user 

# Operations supported by our program are :
#     1: Display number of elements in the capitals collection
#     2: Add an element to the capitals collection like --> Afghanistan: Kabul
#     3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella
#     4: Remove an element from the collection 	
#     5: Take a key from the user and show value if it is present in the dictionary
#     6: Take a key from the user update it if it is present in the dictionary or add the key to the dictionary 	


# Keep asking the user for the operation in this store untill he chooses to exit from the program


def dict_display_capitals(capitals):
    for key, value in capitals.items():
        print(f"The capital of {key} is {value}.")

def dict_add_element(capitals):
    country = input("Enter the country name: ")
    capital = input("Enter the capital city: ")
    capitals[country] = capital
    print(f"Successfully added {country} to the dictionary.")

def dict_add_elements(capitals):
    more_elements = input("Do you want to add more elements? (yes/no): ")
    while more_elements.lower() == 'yes':
        country = input("Enter the country name: ")
        capital = input("Enter the capital city: ")
        capitals[country] = capital
        more_elements = input("Do you want to add more elements? (yes/no): ")

def dict_remove_element(capitals):
    country = input("Enter the country name to remove: ")
    if country in capitals:
        del capitals[country]
        print(f"Successfully removed {country} from the dictionary.")
    else:
        print(f"{country} not found in the dictionary.")

def dict_show_value_for_a_key(capitals):
    country = input("Enter the country name to find the capital: ")
    if country in capitals:
        print(f"The capital of {country} is {capitals[country]}.")
    else:
        print(f"{country} not found in the dictionary.")

def dict_update_or_add_a_key(capitals):
    country = input("Enter the country name to update or add: ")
    if country in capitals:
        capital = input("Enter the new capital city: ")
        capitals[country] = capital
        print(f"Successfully updated {country} in the dictionary.")
    else:
        capital = input("Enter the capital city: ")
        capitals[country] = capital
        print(f"Successfully added {country} to the dictionary.")

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
    capitals = {}
    while True:
        user_input = input("Choose an option: \n1. Add element\n2. Add multiple elements\n3. Remove element\n4. Display capital\n5. Update or add element\n6. Display all capitals\n7. Exit\n")
        if user_input == '1':
            dict_add_element(capitals)
        elif user_input == '2':
            dict_add_elements(capitals)
        elif user_input == '3':
            dict_remove_element(capitals)
        elif user_input == '4':
            dict_show_value_for_a_key(capitals)
        elif user_input == '5':
            dict_update_or_add_a_key(capitals)
        elif user_input == '6':
            dict_display_capitals(capitals)
        elif user_input == '7':
            print("Exiting the program...")
            break
        else:
            print("Invalid option, please try again.")
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display all elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            dict_show_value_for_a_key(capitals)
        elif choice ==6:
            dict_update_or_add_a_key(capitals)
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_dict_store()
