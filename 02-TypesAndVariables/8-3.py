temperature = int(input('Enter the temperature(Celsius): '))
f = float((temperature * 9/5) + 32)
k = float(temperature + 273.15)
print(f'The tempetarure in Celsius is {temperature}, in Fahrenheit is {f:.2f} and in Kelvin is {k:.2f}')
