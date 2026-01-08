def f(expression):
    numbers = {'1','2','3','4','5','6','7','8','9','0'}
    stack = []
    for i in expression.split():
        if i in numbers:
            stack += [int(i)]
        elif i in {'+','-','*','/'}:
            b = stack.pop()
            a = stack.pop()
            if i == "+":
                stack += [a+b]
            elif i == "-":
                stack += [a-b]
            elif i == "*":
                stack += [a*b]
            elif i == "/":
                stack += [a/b]
        elif i == "=":
            return stack.pop()
            
print(f("2 3 + ="))
print(f("2 4 1 + * ="))