import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = [1,1.5,3,5,3.5,4.5,3.5]
x2 = [1,2,4,7,5,5,4.5]

k=2

c1x1 = 1
c1x2 = 1
c2x1 = 5
c2x2 = 7
cl1x1= []
cl1x2= []
cl2x1= []
cl2x2= []
newc1x1=0


for j in range (5):
    for i in range(np.size(x1)):
        d1 = np.sqrt((c1x1-x1[i])**2+(c1x2-x2[i])**2)
        d2 = np.sqrt((c2x1-x1[i])**2+(c2x2-x2[i])**2)
        #print
        m = min(d1,d2)
        if min(d1,d2)==d1:
            print (i)
            cl1x1.append(x1[i])
            cl1x2.append(x2[i])
        else:
            print (i)
            cl2x1.append(x1[i])
            cl2x2.append(x2[i])


plt.scatter(cl1x1, cl1x2)
plt.scatter(cl2x1, cl2x2)
plt.show()

newc1x1 = np.mean(cl1x1)
newc1x2 = np.mean(cl1x2)
newc2x1 = np.mean(cl2x1)
newc2x2 = np.mean(cl2x2)
print ("new centroids are :")
print (newc1x1, newc1x2)
print (newc2x1, newc2x2)
c1x1 = newc1x1
c1x2 = newc1x2
c2x1 = newc2x1
c2x2 = newc2x2
