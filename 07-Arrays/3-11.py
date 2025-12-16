def bubblesort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # swap elements
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

# Arrays to be sorted
arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [15, -3, 22, 8, 0, 7]
arr3 = [100, 50, 75, 25, 10]

print("Original:", arr1)
print("Sorted:", bubblesort(arr1.copy()))

print("Original:", arr2)
print("Sorted:", bubblesort(arr2.copy()))

print("Original:", arr3)
print("Sorted:", bubblesort(arr3.copy()))