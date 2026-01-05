arr1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arr2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

def f(array):
    array2 = []
    for j in range(len(array[0])):
        row = []
        for i in range(len(array)):
            row.append(array[i][j])
        array2.append(row)
            

    result = ''
    for i in array2:
        for j in i:
            result += str(j) + ' '
        result += '\n'
    return result

if __name__ == "__main__":
    print(f(arr1))
    print(f(arr2))