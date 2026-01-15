def f(expression):
    import queue
    result = queue.LifoQueue()
    for i in expression.split():
        x = 0
        y = 0
        if i != " ":
            if i != '+' and i!= '-':
                result.put(int(i))
            else:
                if i == '+':
                    x = result.get()
                    y = result.get()
                    result.put(x+y)
                elif i == '-':
                    x = result.get()
                    y = result.get()
                    result.put(y-x)
    
    return result.get()

if __name__ == "__main__":
    print(f("2 3 +")) 
    print(f("2 6 + 4 5 - +")) 
    print(f("11 7 + 15 - 14 +"))