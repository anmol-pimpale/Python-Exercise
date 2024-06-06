#1.2) Create a program named "my_tuple_store"

def tuple_display_members(members):
    print("The tuple members are:", members)

def display_3_4_5_element(members):
    if len(members) < 5:
        print("Not enough elements in the tuple")
    else:
        print("Element 3:", members[2])
        print("Element 4:", members[3])
        print("Element 5:", members[4])

def tuple_retrieve_element(members):
    index = int(input("Enter the index of the element you want to retrieve: "))
    if index < 0 or index >= len(members):
        print("Index out of range")
    else:
        print("Element at index", index, "is:", members[index])

def tuple_retrieve_elements(members):
    start = int(input("Enter the starting index: "))
    end = int(input("Enter the ending index: "))
    if start < 0 or end > len(members) or start >= end:
        print("Index out of range")
    else:
        print("Elements from index", start, "to index", end, "are:", members[start:end])

def find_min_element(members):
    if len(members) == 0:
        print("Empty tuple")
    else:
        min_value = members[0]
        for i in range(1, len(members)):
            if members[i] < min_value:
                min_value = members[i]
        print("The minimum element is:", min_value)

def reverse_tuple(members):
    print("Reversed tuple is:", members[::-1])

def my_tuple_store():
    print("\n Welcome to Our tuple Store !!! ")
    print("Please enter a tuple Comma seperated that you would want to perform Operation Upon")
    members = tuple(input("Enter the elements:\n").split(","))

    while True:
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display all elements of the tuple")
        print("  2:  Display third, fourth and fifth element from the collection ")
        print("  3:  Retrieve element at a given subscript")
        print("  4:  Retrieve elements from a given subscript and to a given subscript")
        print(" 5:	 Find minimum element in the tuple ")
        print(" 6:	 Reverse elements in the tuple ")
        print("  7: Exit the Program ")
        choice = int(input("Please enter your choice "))

        if choice == 1:
            tuple_display_members(members)
        elif choice == 2:
            display_3_4_5_element(members)
        elif choice == 3:
            tuple_retrieve_element(members)
        elif choice == 4:
            tuple_retrieve_elements(members)
        elif choice == 5:
            find_min_element(members)
        elif choice == 6:
            reverse_tuple(members)
        elif choice == 7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_tuple_store()