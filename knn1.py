import numpy as np
import math
import statistics as st
import matplotlib.pyplot as plt

x1 = [3.393533, 3.110073, 1.343809, 3.582294, 2.280362, 7.423437, 5.745052, 9.172169, 7.792783, 7.939821]
x2 = [2.3313, 1.7815, 3.3684, 4.6792, 2.867, 4.6965, 3.534, 2.5111, 3.4241, 0.7916]
y = [0,0,0,0,0,1,1,1,1,1]

x1new=6
x2new=3

a=[]
b=[]
Sumab=[]
Dist=[]
for i in range(len(x1)):
    a=((x1[i]-x1new)*(x1[i]-x1new))
    b=((x2[i]-x2new)*(x2[i]-x2new))
    sumab=a+b
    Sumab.append(sumab)
    dist=math.sqrt(sumab)
    Dist.append(dist)
    print(a,b)
    print(Sumab)
    print(Dist)

for i in range(len(Dist)):
    for j in range(len(Dist)-i-1):
        if Dist[j]>= Dist[j+1]:
            Dist[j],Dist[j+1]=Dist[j+1],Dist[j]
            y[j],y[j+1]=y[j+1],y[j]

print(Dist)
print(y)

k=6
y_p=[]
for i in range (0,k):
    y_p.append(y[i])
n=st.mode(y_p)
print(n)

plt.scatter(x1,x2)
plt.xlabel(y_p,color='y')
plt.show()




