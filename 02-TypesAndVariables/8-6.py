distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter the fuel consumption in liters per 100 km: '))
total_fuel_consumption = (fuel_consumption * distance)/100
total_cost = total_fuel_consumption * fuel_price
print(f'The total fuel consumption is: {total_fuel_consumption}')
print(f'The total cost is: {total_cost}')