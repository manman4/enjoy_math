import mpmath
import matplotlib.pyplot as plt

x = []
y = []

# 1をm等分
m = 100
# 1/m
interval = 0.01
n = 150
t = range(0, n * m)

for q in t:
    s = 0.5 + interval * t[q] * 1j
    x.append(0.01 * t[q])
    y.append(abs(mpmath.zeta(s)))

fig = plt.figure(figsize = (10, 8))
ax = fig.add_subplot(111)
ax.set_title("Absolute value of Riemann zeta Function", size = 14)
ax.grid()
ax.set_xlim(0, n)
ax.set_ylim(-1, 5)
ax.set_xlabel("Critical Line", size = 14, labelpad = 10)
ax.set_ylabel("|ζ(s)|", size = 14, labelpad = 10)
ax.plot(x, y, color = "darkblue")

# 描画より先に保存しないと真っ白
plt.savefig("img.png")
plt.show()