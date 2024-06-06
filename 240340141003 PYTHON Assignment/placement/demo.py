
def check_numbers(a):
    if len(a) == len(set(a)):  #we use set because inside set duplicate are not allow  here we check the condition
        return "All numbers are unique."
    else:
        return "There are duplicate numbers."

a = input("Enter the numbers separated by spaces: ") # taking input from user
a = list(map(int, a.split()))  #we use the split fuction for spliting the string  and map fuction converting a string into int
print(check_numbers(a))  #we call the our fuction which is use