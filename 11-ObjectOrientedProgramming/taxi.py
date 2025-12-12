class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
        fare = self.calculate_fare()
        print(f"Receipt for the ride:")
        print(f"Distance: {self.distance} km")
        print(f"Rate: ${self.rate_per_km}/km")
        print(f"Fare: ${fare}")
        print("-" * 30)

def main():
    ride1 = TaxiRide(3, 10)  # 10 km at $2.5/km
    ride2 = TaxiRide(5, 20)  # 15 km at $3.0/km

    # Calculate fares and print receipts
    ride1.print_receipt()
    ride2.print_receipt()
        

    
if __name__ == "__main__":
    main()
