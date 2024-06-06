def check_numbers(numbers):
    l1 = []
    for a in numbers:
        if a not in l1:
            l1.append(a)
        else:
            return "There are duplicate numbers."
    return "All numbers are unique."

a = input("Enter the numbers separated by spaces: ")
a = list(map(int, a.split()))

print(check_numbers(a))