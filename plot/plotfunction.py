#function 2x^2-5x+1

import numpy as np
import matplotlib.pyplot as plt

beg=-1000
end=1000
leng=200000
ArrLine=np.arange(-(leng/2),leng/2)
Base_axis=np.zeros(leng)
#draw x-axis and y-axis
plt.plot(Base_axis,ArrLine,'k')
plt.plot(ArrLine,Base_axis,'k')

x=np.linspace(beg,end,leng)
y=list()
d=list()

for i in range(leng):
    y.append(2*(x[i]**2)-5*x[i]+1)
    d.append(4*x[i]-5)

y=np.array(y)

f=plt.plot(x,y)

dx=plt.plot(x,d,'r',)
plt.axis([-5,5,-5,5])
plt.show()