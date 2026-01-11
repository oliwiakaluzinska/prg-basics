def is_even(number):
    mean = lambda x: x % 2 ==0
    result = mean(number)
    return result

print(is_even(7))