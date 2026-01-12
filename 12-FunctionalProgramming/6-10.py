import matplotlib.pyplot as plt

# dane temperatur
temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

# użycie map() do przygotowania list danych
cities = list(map(lambda x: x, temps.keys()))
temperatures = list(map(lambda x: temps[x], temps.keys()))

# tworzymy wykres słupkowy
plt.bar(cities, temperatures, color='skyblue')

# tytuł i opisy osi
plt.title("Temperatures in Polish Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")

# pokazujemy wykres
plt.show()