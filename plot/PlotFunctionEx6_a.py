# plot function f(x)=sqrt(x+2)
import numpy as np
import matplotlib.pyplot as plt
import math
beg=0
end=1000
leng=2000
base_axis=np.zeros(leng)
x=np.linspace(beg,end,leng)
y=list()
for i in x:
    y.append(math.sqrt(i+2))

f=np.array(y)

plt.plot(x,f,'b')
plt.plot(x,base_axis,'k')
plt.plot(base_axis,x,'k')
plt.axis([0,100,0,10])

plt.yticks(range(0,11,1))
plt.xticks(range(0,101,5))
plt.title('f(x)=sqrt(x+2)')
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()
    
