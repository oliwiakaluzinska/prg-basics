def f(array):
    minimum = array[0][0]
    for i in array:
        for j in i:
            if j < minimum:
                minimum = j

    for x in range(len(array)):
        for y in range(len(array[x])):
          if minimum == array[x][y] and x == y:
            return True
    return False
        
if __name__ == "__main__":
    print(f([[7,8],[5,3],[9,4]]))  
    print(f([[7,8,5,3],[9,4,2,6]]))