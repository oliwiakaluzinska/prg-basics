def f(name):
    with open(name) as file:
        content = file.read()
    return content

file_content = f('pets.txt')
print(file_content)
file_content = file_content.split()

print(len(file_content))