__author__ = 'student'
import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.errorbar(x, y,linestyle='None', xerr=[0.1, 0.02, 0.5, 0.2, 0.1], yerr=[0.1,0.2,0.1,0.2,0.1])
plt.grid()
#x = [1, 2, 3, 4, 5, 6]
#y = [1, 1.42, 1.76, 2, 2.24, 2.5]
x1=np.arange(0,7,0.01)
v, p = np.polyfit(x, y, deg=3, cov=True)
p_f = np.poly1d(v)

plt.plot(x1, p_f(x1))
plt.show()