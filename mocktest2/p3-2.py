def f(array2D):
    n = 0
    for i in range(len(array2D)):
        sum_column = 0
        sum_row = sum(array2D[i])
        for j in range(len(array2D)):
            sum_column += array2D[j][i]
        if sum_row == sum_column:
            n += 1

    if n == len(array2D[0]):
        return True
    else:
        return False
    
if __name__ == "__main__": 
    print(f([[3,7,2],[4,2,5],[5,2,1]])) 
    print(f([[3,7,2],[4,2,5],[9,2,1]]))