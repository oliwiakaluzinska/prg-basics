arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
]

def f(array):
    for i in array:
        i[0],i[-1] = i[-1],i[0]
    
    result = ''
    for row in array:
        for x in row:
            result += str(x) + " "
        result += "\n"
    return result
if __name__ == "__main__":
    print(f(arr))