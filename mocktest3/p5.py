def f(mnumbers):
    import re
    pattern = '^[+-]?[A-Da-d1-7]+$'
    
    number = 0
    for i in mnumbers:
        if re.match(pattern, i):
            number +=1
    return number

print(f(["A15","-31","7abC","+D1","-g4"]))