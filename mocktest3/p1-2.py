def f(word):
    word = str(word)
    result = ''
    for i in range(len(word)):
        result+= word[:i] + word[i].upper() + word[i+1:]
        if word[i] == word[-1]:
            break
        result += "-"
    return result

print(f("water"))
print(f("A"))
print(f(""))
print(f("kupa"))