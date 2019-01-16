import math 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

xP=1
yP=1

beg=-1000
end=1000
leng=200000

x=np.linspace(beg,end,leng)
y=f(x)

lim=2

tangent= lim*(x-1)+1

plt.plot(x,tangent)
plt.plot(x,y)
plt.grid()
plt.axis([-100,100,-100,100])
plt.show()

