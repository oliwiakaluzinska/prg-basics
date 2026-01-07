text = 'integers.txt'

with open(text, 'w', encoding='utf-8') as file:
    for i in range(1,101):
        line = (f'{i}, {i**2}, {i**3}')
        print(line)
        file.write(line + '\n')