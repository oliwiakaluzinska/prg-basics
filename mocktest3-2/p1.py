def f(n):
    arr = []
    n = str(n)
    for i in n:
        if int(i) % 2 != 0:
            arr.append(int(i))
    if arr == []:
        return -1
    else:
      return max(arr)-min(arr)

if __name__ == "__main__":
    print(f(10852)) 
    print(f(723597))
    print(f(4388))
    print(f(846206))