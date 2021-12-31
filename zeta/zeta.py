import mpmath
mpmath.mp.dps = 25
mpmath.mp.pretty = True

for i in range(-6, 8, 2):
    print([i, mpmath.zeta(i)])

