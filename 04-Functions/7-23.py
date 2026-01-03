def f(password):
    if len(password)<6:
        return False
    else:
        for i in range(len(password)):
            for j in range(len(password)):
                if i != j and password[i] == password[j]:
                    return False
    return True
if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f(""))