arr = [
       [-38, 19], 
       [5,40],
       [-7,11],
       [29,16]
       ]
def f(array):
    max = 0
    min = 0
    for i in array:
        for j in i:
            if j > max:
                max = j
            if j < min:
                min = j
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == max:
                row_max = i
                col_max = j
            if array[i][j] == min:
                row_min = i
                col_min = j
    return (f'Max: {max},{row_max},{col_max}; Min: {min},{row_min},{col_min}')

if __name__ == "__main__":
    print(f(arr))