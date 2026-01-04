def star(n):
    lista = []
    for i in n:
        lista.append(i*'*')
    result = []
    for i in range(len(n)):
        result.append(f'{n[i]}: {lista[i]}')
    return '\n'.join(result)

arr = [2, 6, 4, 9, 7]   
if __name__ == "__main__":
    print(star(arr))