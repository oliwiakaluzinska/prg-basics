def f(data,order):
    if order == 1:
        result = sorted(list(lambda x:x['id'], data))
    elif order == 2:
        result = sorted(list(lambda x:x['points'], data), reverse=True)
    return result

if __name__ == "__main__":
    c = [{'id':"abcd",'points':30},{'id':'oprs','points':20},{'id':'fghi','points':40}]
    print(f(c,1))
    print(f(c,2))