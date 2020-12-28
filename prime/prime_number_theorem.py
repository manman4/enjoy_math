import is_prime as ispr
import math
import matplotlib.pyplot as plt

x1, y1 = [], []  # y = pi(x) (xまでの素数の個数) の座標群
x2, y2 = [], []  # y = x / log(x) の座標群
pi = 0

for n in range(2, 1000001):
    if ispr.is_prime(n):
        pi += 1

    x1.append(n)
    y1.append(pi)

    x2.append(n)
    y2.append(n / math.log(n))

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()