arr1 = [
    [2, 3],
    [1, 5]
]

arr2 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

def f(array):
    array2 = []
    for i in array:
        for j in i:
            array2.append(j)
    
    result = ''
    for i in array2:
        result += str(i) + " "
    return result

if __name__ == "__main__":
    print(f(arr1))
    print(f(arr2))