import matplotlib.pyplot as plt
import numpy as np
from math import *

r=1
beg=-2*pi
end=2*pi
leng=2*180*2

theta=np.linspace(beg,end,leng)
x,y=list(),list()
for i in theta:
    x.append(r*(i-sin(i)))
    y.append(r*(i-cos(i)))

plt.plot(x,y,'r-',markersize=1)
plt.plot(r*(0-sin(0)),r*(0-cos(0)),'ro')
plt.grid()
plt.show()
