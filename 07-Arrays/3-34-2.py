def f(n):
    array = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i == j:
                array[i][j] = 1

    result = ''
    for i in array:
        for j in i:
            result += str(j) + ' '
        result += '\n'
    return result

if __name__ == "__main__":
    print(f(3))
    print(f(5))
    print(f(8))