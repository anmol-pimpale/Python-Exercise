
# 3)  Create a program named "my_set_store" which support following operations on two sets
#     provided by user 

# for ex: 
# 	A = {1,2,3,4,5}
# 	B = {18,19,20,21}
# is provided by the user

# Operations supported by our program are :
# 	1: Union
# 	2: Intersection 
# 	3: A-B
# 	4: B-A
# 	5: Take a element from user and Display if that element is a member of set B 
# 	6: Display number of elements in the set A
#     7: Display number of elements in the set B
# 	8: Add an element taken from the user to the set A
# 	9: Add multiple elements taken from the user to the set A
# 	10: Remove an element taken from the user from set A


def set_union(setA, setB):
    
    return setA.union(setB)

def set_intersection(setA, setB):
    
    return setA.intersection(setB)

def set_minus(setA, setB):
    
    return setA.difference(setB)

def is_member_of_set(setB, element):
    
    return element in setB

def set_display(setA):
    
    print(setA)

def set_add_element(setA, element):
    
    setA.add(element)

def set_add_elements(setA, elements):
    
    setA.update(elements)

def set_remove_element(setA, element):
    
    setA.remove(element)

def my_set_store():
    
    setA = set(input("Please enter comma separated elements for the set A: ").split(","))
    setB = set(input("Please enter comma separated elements for the set B: ").split(","))

    while True:
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("	1: Union")
        print("	2: Intersection ")
        print("	3: A-B")
        print("	4: B-A")
        print("	5: Take a element from user and Display if that element is a member of set B ")
        print("	6: Display number of elements in the set A")
        print(" 7: Display number of elements in the set B")
        print("	8: Add an element taken from the user to the set A")
        print("	9: Add multiple elements taken from the user to the set A")
        print("	10: Remove an element taken from the user from set A")
        print(" 11: Exit")


        choice = int(input("Please enter your choice "))

        if choice == 1:
            set_display(set_union(setA, setB))
        elif choice == 2:
            set_display(set_intersection(setA, setB))
        elif choice == 3:
            set_display(set_minus(setA, setB))
        elif choice == 4:
            set_display(set_minus(setB, setA))
        elif choice == 5:
            element = input("Please enter the element to check: ")
            set_display(is_member_of_set(setB, element))
        elif choice == 6:
            set_display(len(setA))
        elif choice == 7:
            set_display(len(setB))
        elif choice == 8:
            element = input("Please enter the element to add: ")
            set_add_element(setA, element)
        elif choice == 9:
            elements = input("Please enter the elements to add (comma separated): ").split(",")
            set_add_elements(setA, elements)
        elif choice == 10:
            element = input("Please enter the element to remove: ")
            set_remove_element(setA, element)
        elif choice == 11:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")
my_set_store()