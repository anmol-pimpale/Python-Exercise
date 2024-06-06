# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation
# We need to keep executing my_calculator function 
# untill user choose to skip the application



def my_calculator():
    
     while True:
      print("enter the choice")
      print("1.Addition")
      print("2.Squaring")
      print("3.Exponenation")
      print("4.exit")
    
   
      choice=int(input("Enter the choice:"))
      if choice == 1:
            number1=int(input("enter the first number:"))
            number2=int(input("enter the second number:"))
            addition=number1 + number2
            print(f"The result is {addition}")
        
      elif choice == 2:
            num=float(input("enter the number:"))
            squaring= num ** 2
            print(f"the result is {squaring}")
            
            
      elif choice == 3:
            base=float(input("enter the base number:"))
            exp=float(input("enter the exp number:"))
            exponention= base ** exp
            print(f"the exp result is {exponention}")
            
      else:
          return
      print("Do you want to continue? (yes/no)")
      
      user_input = input().lower()
      if user_input != 'yes':
            return

 
        
        
my_calculator()