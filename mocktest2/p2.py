def f(arr):
    inna = arr[0]
    for i in arr:
        if i !=  inna:
            return i 
if __name__ == "__main__": 
    print(f([7,7,7,7,7,9,7,7]))