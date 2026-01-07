def f(email):
    import re
    with open(email, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    pattern = r'From:.*<([^>]+)>'
    for line in lines:
        if pattern == line:
            return line
                
print(f('email.txt'))
