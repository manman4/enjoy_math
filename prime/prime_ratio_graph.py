import is_prime as ispr
import math
import matplotlib.pyplot as plt

x1, y1 = [], []
pi = 0

for n in range(2, 1000001):
    if ispr.is_prime(n):
        pi += 1

    if n % 100 == 0:
        x1.append(n)
        y1.append(n / (math.log(n) * pi))

plt.plot(x1, y1)
plt.show()