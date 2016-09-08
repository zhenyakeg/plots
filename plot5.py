__author__ = 'student'
import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5, 6]
y = [0.99, 0.49, 0.35, 0.253, 0.18, 0.22]
plt.errorbar(x, y,linestyle='None', xerr=[0.1, 0.02, 0.5, 0.2, 0.1, 0.3], yerr=[0.1,0.2,0.2,0.1,0.2,0.1])
plt.grid()
#x = [1, 2, 3, 4, 5, 6]
#y = [1, 1.42, 1.76, 2, 2.24, 2.5]
x1=np.arange(0,7,0.01)
v1, p1 = np.polyfit(x, y, deg=1, cov=True)
p_f1 = np.poly1d(v1)
v2, p2 = np.polyfit(x, y, deg=2, cov=True)
p_f2 = np.poly1d(v2)
plt.plot(x1, p_f1(x1))
plt.plot(x1, p_f2(x1))

plt.show()