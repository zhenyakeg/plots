__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt
a=10
b=0.5
x=np.arange(0,7,0.01)
n=0
y=0
while n<300:
    y+=b**n*np.cos(a**n*np.pi*x)
    n+=1

plt.plot(x,y)
plt.show()