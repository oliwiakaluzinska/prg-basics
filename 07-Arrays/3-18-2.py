def f1(array):
    max1 = 0
    max2 = 0
    for i in array:
        if i > max1:
            max1 = i
    for j in array:
        if j > max2 and j < max1:
            max2 = j
    return max2

def f2(array):
    max = array[0]
    min = array[0]
    for i in array:
        if i > max:
            max = i
    for j in array:
        if j < min:
            min = j
    return max - min

def f3(array):
    array = sorted(array)
    if len(array)%2 == 0:
        x = (array[len(array)//2] + array[(len(array)//2 - 1)])/2
        return x
    else:
        return array[len(array)//2]

def f4(array):
    add = []
    max = array[0]
    min = array[0]
    for i in array:
        if i > max:
            max = i
    for j in array:
        if j < min:
            min = j
    add.append(max)
    add.append(min)
    return add

def f5(array):
    add = []
    for i in array:
        i = str(i)
        add.append(i)
    return "-".join(add)

if __name__ == "__main__":
    print(f1([7,3,8,5,2]))
    print(f2([7,3,8,5,2]))
    print(f3([7,3,8,5,2]))
    print(f4([7,3,8,5,2]))
    print(f5([7,3,8,5,2]))