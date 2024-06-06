#Take two int values from user and print greatest among them

def gretest_number(a,b):
    if(a>b):
        return a
    
    else:
        return b
    
    
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
greatest=gretest_number(a,b)

print("The greatest number is:", greatest)
    