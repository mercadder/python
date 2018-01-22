#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


N = 10
y = np.zeros(N)
y1 = np.linspace(0, 10, 100)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 5, N, endpoint=False)
x3 = np.linspace(0, 10, N, endpoint=True)


plt.plot(x1, y, '.')
plt.plot(x3, y + .4, 'o')
plt.plot(x2, y + .8, '*')
plt.plot(y1, np.cos(y1 * np.pi / 4), '-')
plt.ylim([-5, 5])

plt.show()
