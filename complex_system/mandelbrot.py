#############
#
# conda install numba
#
#############

import numpy as np
from numba import jit
import matplotlib.pyplot as plt

# const
columns = 3000
rows = 3000

@jit
def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j

    for i in range(max_iter):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i
    return max_iter

result = np.zeros([rows, columns])
for row_index, Re in enumerate(np.linspace(-2, 1, num=rows)):
    for column_index, Im in enumerate(np.linspace(-1, 1, num=columns)):
        result[row_index, column_index] = mandelbrot(Re, Im, 100)

plt.figure(dpi=120)
plt.imshow(result.T, cmap='bone', interpolation='bilinear', extent=[-2, 1, -1, 1])
plt.xticks(color='None')
plt.yticks(color='None')
plt.tick_params(length=0)
plt.show()
plt.savefig('figure.png')