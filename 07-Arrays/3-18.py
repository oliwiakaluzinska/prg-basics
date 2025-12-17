arr = [7,3,8,5,2]
def f1(array):
    max = array[0]
    for i in array:
        if i > max:
            max = i
    array.remove(max)
    max1 = array[0]
    for i in array:
        if i > max1:
            max1 = i
    return max1
print(f1(arr))

arr = [7,3,8,5,2]
def f2(array):
    min = array[0]
    max = array[0]
    for i in array:
        if i > max:
            max = i
        if i < min:
            min = i
    x = max - min
    return x
print(f2(arr))

arr = [7,3,8,5,2]
def f3(array):
    n = len(array)
    sorted_arr = sorted(array)

    # If the number of elements is odd
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:  # if even, average the two middle elements
        mid1 = sorted_arr[n // 2 - 1]
        mid2 = sorted_arr[n // 2]
        return (mid1 + mid2) / 2
print(f3(arr))

arr = [7,3,8,5,2]
def f4(array):
    min = array[0]
    max = array[0]
    for i in array:
        if i > max:
            max = i
        if i < min:
            min = i
    x = [min, max]
    return x
print(f4(arr))

arr = [7,3,8,5,2]
def f5(array):
    result = ""  # pusty napis na start
    for i in range(len(array)):
        result += str(array[i])
        if i != len(array) - 1:  # jeśli to nie ostatni element, dodaj myślnik
            result += "-"
    return result
print(f5(arr))