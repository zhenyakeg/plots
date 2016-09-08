__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-100,100,0.1)
plt.xkcd()
plt.plot(eval(input()))

#plt.plot((np.log((x**2+1)*np.exp(-np.abs(x)/10)))/(np.log(1+np.tan(1/(1+(np.sin(x))**2)))))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
#plt.title(r'$x^2-x-6$')
plt.grid(True)

plt.show()
