#1) Accept two numbers from the user and print 
#a) addition 
#b) first number squared 2 
#c) first number raised to second number

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print('The sum of {} and {} is {}'.format(num1, num2, num1 + num2))
print(' The square of {} is {}'.format(num1, num1 ** 2))
print('{} raised to {} is {}'.format(num1, num2, num1 ** num2))
