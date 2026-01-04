def compare(array1, array2):
    x = False
    if len(array1) == len(array2):
        for i in range(len(array1)):
            for j in range(len(array2)):
                if i == j and array1[i] == array2[j]:
                    x = True
    return x

if __name__ == "__main__":
    print(compare(["water","book","sky"], ["water","book","sky"]))
    print(compare([True,False] ,  [True,False,True]))
    print(compare([5,3,1]  , [5,3,1]))
    print(compare([3,2,1] ,  [3,2]))