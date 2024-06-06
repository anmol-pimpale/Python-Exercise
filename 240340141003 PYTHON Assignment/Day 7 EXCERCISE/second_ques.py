# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 


class Airline:
    def __init__(self, departure_city, arrival_city, flight_number, seat_assignment):
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.flight_number = flight_number
        self.seat_assignment = seat_assignment
    
    
    def display_ticket_details(self):
        print(f"departure city:{self.departure_city}")
        print(f"arraival_city:{self.arrival_city}")
        print(f"flight_number:{self.flight_number}")
        print(f"seat_assignment:{self.seat_assignment}")
        
ticket1 = Airline("mumbai", "banglore", "123", "12F")
ticket2 = Airline("Chicago", "Caneda", "456", "23A")

ticket1.display_ticket_details()
print()
ticket2.display_ticket_details()    
            