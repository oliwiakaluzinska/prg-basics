arr = [4,36,12,28,9,44,5]

def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j+1],array[j] = array[j],array[j+1]
    return array

if __name__ == "__main__":
    print(bubblesort(arr))