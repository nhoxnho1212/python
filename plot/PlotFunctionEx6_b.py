# plot function f(x)=1/(x^2-x)
import numpy as np
import matplotlib.pyplot as plt
import math
beg=-10
end=10
leng=200000
base_axis=np.zeros(leng)
x=np.linspace(beg,end,leng)
y=list()
for i in x:
    y.append(1/(i**2-i))

f=np.array(y)

plt.plot(x,f,'r,')
plt.plot(x,base_axis,'k',linewidth=0.1)
plt.plot(base_axis,x,'k',linewidth=0.1)
plt.axis([-5,5,-5,5])

#plt.yticks(range(0,11,1))
#plt.xticks(range(0,101,5))
plt.title('f(x)=1/(x^2-x)')
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()
    
