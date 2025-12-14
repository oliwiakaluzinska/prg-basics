def check_all_equal(n1, n2, n3):
    if n1 == n2 and n2 == n3 and n1 == n3:
        f = True
    else:
        f = False
    return f
if __name__ == '__main__':
    print(check_all_equal(4,8,5))
    print(check_all_equal(2,2,2))

