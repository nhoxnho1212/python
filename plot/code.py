import math 

def fpenis(i):
    a=list()
    for x in i:
        a.append(abs(math.sin(x)+5*math.exp(-x**100)*math.cos(x)))
    return a
import numpy as np
import matplotlib.pyplot as plt

beg=-3
end=3
leng=200000

x=np.linspace(beg,end,leng)
y=fpenis(x)


plt.plot(x,y,'r.',markersize=1)
plt.axis([-3,3,0,5.1])
plt.text(-2.9,-3,r'CODE')
plt.grid(True)
plt.show()
