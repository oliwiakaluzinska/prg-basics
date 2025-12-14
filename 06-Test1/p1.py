def f(tree_circumference):
    import math
    srednica = tree_circumference / math.pi
    if srednica >= 50:
        x = True
        return x
    else:
        x = False 
        return x
if __name__ == "__main__":
    print(f(100))
    print(f(200))