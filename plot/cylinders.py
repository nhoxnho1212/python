#plot function z=x^2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

beg_y=-20
end_y=20
leng=40



x=list()
y=list()
for i in range(-20,20,1):
    y.append(np.full((leng,leng),i))
    x.append(np.linspace(beg_y,end_y,leng))

y=np.array(y)
x=np.array(x)
z=x**2
mpl.rcParams['legend.fontsize'] = 10
ax.plot(x,y,z)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
