def  f(car,order):
    arr1 = []
    arr2 = []
    if order == 1:
        return sorted(car, key=lambda d: list(d.keys())[0])
    elif order == 2:
        return sorted(car, key=lambda d: list(d.values())[0], reverse=True)
if __name__ == "__main__":
    cars = [{"KR333":138},{"WL555":497},{"DB444":341},{"MC222":412}]
    print(f(cars,1))
    print(f(cars,2))