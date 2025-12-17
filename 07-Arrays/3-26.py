import matplotlib.pyplot as plt
import math 
x = []
y = []

for i in range(0, 361):
    x.append(i)
    y.append(math.sin(math.radians(i)))

plt.plot(x, y)
plt.show()