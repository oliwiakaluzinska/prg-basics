def f(text):
    import queue
    reverse = queue.LifoQueue()
    for i in text:
        reverse.put(i)
    
    result = ''
    while not reverse.empty():
        result += str(reverse.get())
    return result
text = input('Enter text: ')
print(f(text))