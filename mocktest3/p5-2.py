def f(mnumbers):
    import re
    pattern = '^[-+]?[1-7a-dA-D]+$'
    result = 0
    for i in mnumbers:
        if re.match(pattern, i):
            result += 1
    return result

if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-g4"]))
