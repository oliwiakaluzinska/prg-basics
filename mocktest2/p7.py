def f(array):
    import re
    pattern = '^[_a-z0-9]{4,12}$'
    result = 0
    for i in array:
        if re.match(pattern, i):
            result += 1
    return result

if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))