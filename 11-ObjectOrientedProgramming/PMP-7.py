class Statistics:
    def __init__(self):
        self.arr = []
        self.max = 0
        self.min = 0
        self.ari = 0
        self.mediana = 0


    def add_no(self, number):
        self.number = number
        self.arr.append(self.number)

    def show_numbers(self):
        print(', '.join(str(x) for x in self.arr))
    
    def max_number(self):
        self.max = max(self.arr)

    def min_number(self):
        self.min = min(self.arr)

    def arithmetic(self):
        self.total = 0
        for i in self.arr:
            self.total += i
        self.ari = self.total / len(self.arr)

    def median(self):
        self.arr = sorted(self.arr)
        if len(self.arr) % 2 == 0:
            self.mediana = (self.arr[len(self.arr)//2] + self.arr[len(self.arr)//2 - 1])/2
        else:
            self.mediana = self.arr[len(self.arr)//2]
    
    def show_status(self):
        print(f'Maximum: {self.max}')
        print(f'Minimum: {self.min}')
        print(f'Arithmetic mean: {self.ari}')
        print(f'Median: {self.mediana}')

def main():
    number = Statistics()
    number.add_no(12)
    number.add_no(37)
    number.add_no(6)
    number.add_no(9)
    number.add_no(17)
    number.show_numbers()
    number.max_number()
    number.min_number()
    number.arithmetic()
    number.median()
    number.show_status()
main()