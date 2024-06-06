# 1. Create a program named "my_list_store"
# which support following operations on list named "members" which is provided by the user 
# for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania is provided by the user 

# Operations supported by our program are :
#   1:  Display all the elements in the members list
#   2:  Add an element to the members collection like 'Sehwag' 
#   3:  Add elements to the members collection like ['David','Bret','Sanju']
#   4:  Remove a member from the collection at a given subscript
#   5:  Remove the last member from the collection 
#   6:  Display third, fourth and fifth element from the collection 

# Keep asking the user for the operation in this store untill he chooses to exit from the program

def list_display_members(members) :
	print("Member list",members)

def list_add_element(members) :
  element = input("Enter the element to add: ")
  members.append(element)
  print("Element added successfully!")


def list_add_elements(members):
 element = input("Enter the element to add: ")
 members.extend(element)
 print("Element added successfully!")


def list_remove_element(members) :
 index = int(input("Enter the subscript of the member to remove: "))
 if index >= 0 and index < len(members):
        del members[index]
        print("Member removed successfully!")
 else:
        print("Invalid subscript!")

def remove_last_element(members) :
   if len(members) > 0:
     del members[-1]
     print("Last member removed successfully!")
   else:

    print("The list is already empty!")

def display_3_4_5_element(members):
 if len(members) >= 3:
             print("Third, fourth, and fifth elements: ", members[2:5])
 else:
           print("The list does not have three or more elements!")
			
def my_list_store():
    print("\n Welcome to Our List Store !!! ")
    print("Please enter a list Comma seperated that you would want to perform Operation Upon")
    members = input("please enter strings:").split(",")
    
    
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display all elements in the members list")
        print("  2:  Add an element to the members collection like 'Sehwag' ")
        print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
        print("  4:  Remove a member from the collection at a given subscript")
        print("  5:  Remove the last member from the collection ")
        print("  6:  Display third, fourth and fifth element from the collection ")
        print("  7: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            list_display_members(members) 
        elif choice ==2:
            list_add_element(members) 
        elif choice ==3:
            list_add_elements(members)
        elif choice ==4:
            list_remove_element(members) 
        elif choice ==5:
            remove_last_element(members) 
        elif choice ==6:
            display_3_4_5_element(members) 
        elif choice ==7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_list_store()		