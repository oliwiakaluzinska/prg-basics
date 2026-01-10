class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
        return self.fare
    
    def print_receipt(self):
        fare = self.calculate_fare(self.distance)
        print(f"Receipt for the ride:")
        print(f"Distance: {self.distance} km")
        print(f"Rate: ${self.rate_per_km}/km")
        print(f"Fare: ${fare}")
        print("-" * 30)



    
if __name__ == "__main__":
    def main():
     ride1 = TaxiRide(2.5)  # 10 km at $2.5/km
     ride1.calculate_fare(10)
     ride2 = TaxiRide(3)  # 15 km at $3.0/km
     ride2.calculate_fare(15)
    

    # Calculate fares and print receipts
     ride1.print_receipt()
     ride2.print_receipt()
    main()