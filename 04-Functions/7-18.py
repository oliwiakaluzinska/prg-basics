def f(sentence):
    add = []
    for i in sentence:
        if i != " ":
          add.append(i)

    
    return ''.join(add)

if __name__ == "__main__":
    print(f("integrated development environment"))
    print(f("A programming language is a system of notation for writing computer programs"))