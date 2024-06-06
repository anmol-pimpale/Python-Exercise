# 2) Write a program that creates a list of 5 elements of your choice 
# Now take the index that the user want the data of and print the value at that 
# location 
# Exception handle the code to  terminate gracefully by printing 
# Value not found if the index doesnot exists 


l=["rose","lotus","mogra","Jasmine","Lavender"]

index=int(input("Enter the index:"))

try:
    value=l[index]
    print("the value of that index:",value)
except IndexError:
    print("value not found")
    