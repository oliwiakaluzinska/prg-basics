def f(d):
    result = []
    for i in d:
        if i[1] == 'in':
            result.append(i[0])
        elif i[1] == 'out':
            result.remove(i[0])
    result = sorted(result)
    return result


if __name__ == "__main__":
    cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]] 
    print(f(cars))
    cars1 = [["KR234","in"],["KR234","out"]] 
    print(f(cars1))