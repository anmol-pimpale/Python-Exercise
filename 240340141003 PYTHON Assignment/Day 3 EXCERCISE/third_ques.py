#Take a number from the user and print all Odd numbers from 1 to that number 

def print_odd_numbers(n):
    for i in range(1, n + 1, 2):
        print(i)

num = int(input("Enter a number: "))
print_odd_numbers(num)