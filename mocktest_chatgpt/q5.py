def f(codes):
    import re
    pattern = '^#?[0-5xyzXYZ]+$'
    number = 0
    for i in codes:
        if re.match(pattern, i):
            number += 1
    return number

if __name__ == "__main__":
    codes = ["7xy","#2o","xyz34"]
    print(f(codes))