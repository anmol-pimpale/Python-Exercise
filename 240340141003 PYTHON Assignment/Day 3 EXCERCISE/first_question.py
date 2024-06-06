#Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game


def fizz_buzz():
        
    num = int(input("Please enter the number:"))

    if num %5==0 and num % 3 ==0 :
        print("Fizz Buzz")
    elif num%3 == 0 :
        print("Fizz")
    elif num%5 == 0 :
        print("Buzz")
    else:
        print("Invalid Input")

def play_game():
    while(True):
        fizz_buzz()	
        if input("\n Do you want to continue (Y/N)").lower() == 'n':
            break

# function calls
play_game()  
