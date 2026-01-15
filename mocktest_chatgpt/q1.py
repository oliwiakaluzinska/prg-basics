def f(word):
    result = []
    for i in range(len(word)):
        result.append(str(word[:i]+word[i]+word[i]+word[i+1:]))
    return " ".join(result)

if __name__ == "__main__":
    print(f('cat'))
    print(f('a'))
    print(f(''))
    