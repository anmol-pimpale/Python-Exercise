#1.3) Create a program named "my_string_store"

def string_display(string_input):
    print("Displaying the string: ", string_input)

def display_3_4_5_element(string_input):
    if len(string_input) >= 5:
        print("Third, fourth and fifth elements are: ", string_input[2:5])
    else:
        print("String length is less than 5, cannot display elements 3, 4, and 5")

def string_retrieve_element(string_input):
    index = int(input("Enter the index of the character you want to retrieve: "))
    if index >= 0 and index < len(string_input):
        print("Character at index", index, "is: ", string_input[index])
    else:
        print("Index out of range, please enter a valid index")

def string_retrieve_elements(string_input):
    start_index = int(input("Enter the starting index: "))
    end_index = int(input("Enter the ending index (exclusive): "))
    if start_index >= 0 and end_index > start_index and end_index <= len(string_input):
        print("Substring from index", start_index, "to index", end_index, "is: ", string_input[start_index:end_index])
    else:
        print("Invalid indices, please enter valid indices")

def find_min_element(string_input):
    if len(string_input) == 0:
        print("String is empty, no minimum character")
    else:
        min_char = min(string_input)
        print("Minimum character in the string is: ", min_char)

def reverse_string(string_input):
    reversed_string = string_input[::-1]
    print("Reversed string is: ", reversed_string)

def find_each_character_count(string_input):
    char_count = {}
    for char in string_input:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print("Character counts are: ", char_count)

def find_character_count_greater_than_1(string_input):
    char_count = {}
    for char in string_input:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print("Characters with count greater than 1 are: ", [char for char in char_count if char_count[char] > 1])

def check_palindrome(string_input):
    string_input = string_input.lower()
    if len(string_input) == 0 or len(string_input) == 1:
        print("String is a palindrome")
    else:
        if string_input == string_input[::-1]:
            print("String is a palindrome")
        else:
            print("String is not a palindrome")

def my_string_store():
    print("\n Welcome to Our string Store !!! ")
    string_input = input("Please enter a string that you would want to perform Operation Upon: ").strip()

    while True:
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display the string")
        print("  2:  Display third, fourth and fifth element from the string ")
        print("  3:  Retrieve element at a given subscript")
        print("  4:  Retrieve elements from a given subscript and to a given subscript")
        print("  5:  Find minimum character in the string ")
        print("  6:  Reverse the string ")
        print("  7:  Output list of tuple( character,count) for each characters of the string ")
        print("  8:  Output list of characters of the string that appear more than once ")
        print("  9:  Check if the string is a palindrome and return output message accordingly")
        print(" 10: Exit the Program ")
        choice = int(input("Please enter your choice "))

        
        if choice   ==1:
            string_display(string_input) 
        elif choice ==2:
            display_3_4_5_element(string_input) 
        elif choice ==3:
            string_retrieve_element(string_input)
        elif choice ==4:
            string_retrieve_elements(string_input) 
        elif choice ==5:
            find_min_element(string_input) 
        elif choice ==6:
            reverse_string(string_input) 
        elif choice ==7:
             find_each_character_count(string_input)
        elif choice ==8:
             find_character_count_greater_than_1(string_input)
        elif choice ==9:
             check_palindrome(string_input)
        elif choice ==10:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_string_store()