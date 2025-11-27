###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
import math
def triangle_area(a,b,c):
   s = (a+b+c)/2
   area = math.sqrt(s*(s-a)*(s-b)*(s-c))
   return area

pole1 = triangle_area(3,4,5)
pole2 = triangle_area(5,6,7)
pole3 = triangle_area(7,8,9)


print(f'The area of​a triangle with sides (3,4,5) is {pole1}')
print(f'The area of ​​a triangle with sides (5,6,7) is {pole2:.2f}')
print(f'The area of ​​a triangle with sides (7,8,9) is {pole3:.2f}')