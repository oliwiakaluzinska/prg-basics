def powers_to_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(1, 101):
            line = f"{i},{i**2},{i**3}"
            print(line)          # drukowanie na ekranie
            file.write(line + "\n")  # zapis do pliku


powers_to_file("powers.txt")