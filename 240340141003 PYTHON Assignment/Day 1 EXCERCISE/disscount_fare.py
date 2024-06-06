#Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
#string ex: "Fare from mumbai to pune is 400 INR after applied discount of 5% it is 380 INR"

source=input("Enter the source city name:")
destination=input("Enter the destination city:")
fare=float(input("fare in INR:"))
discount_rate  = float(input("Enter the discout rate:"))

discounted_fare = fare - (fare * discount_rate / 100)
print(f"Fare from {source} to {destination} is {fare} INR after applied discount of {discount_rate}% it is {discounted_fare} INR")