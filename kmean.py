import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('E:\kmean.csv')

x1 = np.array(df['A'])
x2 = np.array(df['B'])
y = np.array(df['subject'])

print(x1,x2,y)

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
