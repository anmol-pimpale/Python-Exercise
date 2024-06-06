#ake a number from the user and print all Even numbers from 1 to that number 

def even_number(n):
    for i in range(2,n+2,2):
        print(i)
        
num=int(input("enter the number:"))
even_number(num)