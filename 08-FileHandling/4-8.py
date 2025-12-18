def f(file):
    with open(file, 'r', encoding='utf-8') as text:
        extensions = text.read()
    
    result = []
    extensions = extensions.split()
    for i in extensions:
        if i[-4:] == ".jpg" or i[-4:] == ".csv" or i[-4:] == ".txt":
            result.append(i)
    return result    
print(f('files.txt'))