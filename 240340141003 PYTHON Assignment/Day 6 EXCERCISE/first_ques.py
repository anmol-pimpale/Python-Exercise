
# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }
# Now take the key as input from the user and print its corresponding colour 
# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )

color_dict = {1: "red", 2: "Blue", 3: "Orange"}


key = int(input("Enter a key: "))

try:
    color = color_dict[key]
    print("The corresponding color is:", color)
except KeyError:
    print("Color not found")