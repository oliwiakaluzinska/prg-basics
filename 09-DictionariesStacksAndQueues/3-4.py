def f(number):
    import queue
    binary = queue.LifoQueue()
    while number != 0:
        r = number % 2
        binary.put(r)
        number = number//2
    result =""
    while not binary.empty():
        result += str(binary.get())
    return result

print(f(18))