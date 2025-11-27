def input_string(message):
    s = input(message)
    return s

def input_integer(message):
    n = int(input(message))
    return n

def input_real(message):
    r = float(input(message))
    return r

def input_boolean(message):
    b = input(message).lower()
    if b == 'y':
            return True
    elif b == 'n':
            return False