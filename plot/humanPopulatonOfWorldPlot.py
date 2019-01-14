# graph human population of the world in 1900 to 2010

import numpy as np
import matplotlib.pyplot as plt

time=np.arange(0,111,10)
population=np.array([1650,1750,1860,2070,2300,2560,3040,3710,4450,5280,6080,6870])

beg=0
end=10000
leng=20000   

tmpy=list()
for i in time:
    tmpy.append(((1.43653)*(1.01395**(i)))*1000)
y=np.array(tmpy)

graph=plt.plot(time,population,'ro')
f=plt.plot(time,y,'b')
plt.axis([0,120,0,7000])

plt.show()