def f(car,order):
    if order == 1:
        car = car.sorted()
    else:
        arr = []
        for key,value in car.items():
            number = max(value)
            arr.append(number)