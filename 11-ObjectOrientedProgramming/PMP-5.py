import random
class TEMP:
    def __init__(self):
        self.temp = 0

    def measures(self):
        self.temp = round(random.uniform(34,42), 1)
        if self.temp >= 41:
            print(f'Temperature: {self.temp}C (CRITICAL TEMPERATURE!!)')
        elif self.temp >= 37:
            print(f'Temperature: {self.temp}C (fever)')
        else:
            print(f'Temperature: {self.temp}C')

def main():
    patient1 = TEMP()
    patient1.measures()
    patient2 = TEMP()
    patient2.measures()
main()