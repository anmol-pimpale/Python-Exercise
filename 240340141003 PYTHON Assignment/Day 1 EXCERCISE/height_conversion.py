# Get the height from the user in cms and display the user height back to console
#in foot/feet and inches eg : 155 in cms displays 5.09 in feet and inches



height_cm = float(input("Enter your height in centimeters: "))
height_inch = height_cm / 2.54


height_feet = int(height_inch / 12)
height_inches = int(height_inch % 12)

print(f"Your height is {height_feet} feet and {height_inches} inches")