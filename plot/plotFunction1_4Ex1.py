
import math
import numpy as np
import matplotlib.pyplot as plt

beg=0
end=2
leng=200000
xr=np.linspace(beg,end,leng)
xl=np.linspace(-end,beg,leng)
x1r=np.linspace(beg,3,leng)
y=1/(xr**3-2) +10
y2=-1/(xl**3+2) +10



#line y=3

plt.plot(xr,y,'ro',markersize=1)
plt.plot(xl,y2,'bo',markersize=1)

plt.axis([-10,10,-10,10])

plt.grid(True)
plt.title('f(x)=3-2^x')
plt.show()