def create_2d_arr(x,y):
    arr = [[0 for i in range(y)] for j in range(x)]
    return arr

print(create_2d_arr(3,5))