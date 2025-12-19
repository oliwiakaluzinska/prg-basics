def f(array2D):
    num_columns = len(array2D[0])
    col_sum = [0] * num_columns
    row_sum = 0
    suma = 0
    for i in array2D:
        for j in range(num_columns):
            col_sum[j] += i[j]
            suma = col_sum[j]
    for i in array2D:
        row_sum += sum(i)
    if suma == row_sum:
        return True
    else:
        return False
    
if __name__ == "__main__": 
    print(f([[3,7,2],[4,2,5],[9,2,1]]))