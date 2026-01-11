def mean(x,y):
   m = (x+y) / 2
   return m

# takes two numbers from keyboard
n1 = int(input('Enter the number 1: '))
n2 = int(input("Enter the number 2: "))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')