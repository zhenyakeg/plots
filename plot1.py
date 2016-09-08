__author__ = 'student'

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-2.1,3.1,0.01)
plt.plot(x, x**2-x-6)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$x^2-x-6$')
plt.grid(True)
plt.show()
