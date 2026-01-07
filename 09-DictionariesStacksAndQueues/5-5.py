paragraph = "cat dog mouse cat rat cat mouse"

def f(text):
    text = str(text)
    text = text.split()
    dic = {}
    for i in text:
        if i in dic:
            dic[i] += 1
        else:
           dic[i] = 1
        
    result = ''
    for x,y in dic.items():
        result += (f'{x}: {y}\n')
    return result

print(f(paragraph))