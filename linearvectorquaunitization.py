import numpy as np
import math
import statistics as st



x1 = [3.393533, 3.110073, 1.343809, 3.582294, 2.280362, 7.423437, 5.745052, 9.172169, 7.792783, 7.939821]
x2 = [2.3313, 1.7815, 3.3684, 4.6792, 2.867, 4.6965, 3.534, 2.5111, 3.4241, 0.7916]
y = [0,0,0,0,0,1,1,1,1,1]

x1new=[3.58229404,7.79278348,7.93982082,3.39353321]
x2new=[0.7916372,2.3312734,2.8669903,4.6791791]
ynew=[0,0,1,1]

L=0.7
a=[]
b=[]
Sumab=[]

for j in range(len(x1)):
    Dist=[]
    for i in range(len(x1new)):
        
        a=(x1[j]-x1new[i])*(x1[j]-x1new[i])
        b=(x2[j]-x2new[i])*(x2[j]-x2new[i])
        sumab=a+b
        Sumab.append(sumab)
        dist=math.sqrt(sumab)
        Dist.append(dist)
        #print(a,b)
        #print(Sumab)
        #print(Dist)

    ##    for i in range(len(Dist)):
    ##        for j in range(len(Dist)-i-1):
    ##            if Dist[j]>= Dist[j+1]:
    ##                Dist[j],Dist[j+1]=Dist[j+1],Dist[j]
    print (Dist)
    a=(min(Dist))
    print("yrchgj",a)
    for s in range (len(Dist)):
            if Dist[s]==a:
                n =s
    if y[j]==ynew[n]:
        bmunewa=x1new[n]+L*(x1[j]-x1new[n])
        bmunewb=x2new[n]+L*(x2[j]-x2new[n])
        print("bmunew::",bmunewa,bmunewb)
    else:
        bmunewa=x1new[n]-L*(x1[j]-x1new[n])
        bmunewb=x2new[n]-L*(x2[j]-x2new[n])
        print(bmunewa,bmunewb)

    x1new[n]=bmunewa
    x2new[n]=bmunewb
    print(x1new,x2new)
    print("--------")
        
    


##if y[0]==ynew[0]:
##    bmunewa=x1new[0]+L*(x1[0]-x1new[0])
##    bmunewb=x2new[0]+L*(x2[0]-x2new[0])
##    print("bmunew::",bmunewa,bmunewb)
##
##else:
##    bmunewa=x1new[0]-L*(x1[0]-x1new[0])
##    bmunewb=x2new[0]-L*(x2[0]-x2new[0])
##    print(bmunewa,bmunewb)
##
##x1new[0]=bmunewa
##x2new[0]=bmunewb
##
##print(x1new,x2new)
##
print("----------------------")
Y_p=[]
pred_y=[]
for j in range(len(x1)):
    Dist=[]
    for i in range(len(x1new)):
        
        a=(x1[j]-x1new[i])*(x1[j]-x1new[i])
        b=(x2[j]-x2new[i])*(x2[j]-x2new[i])
        sumab=a+b
        Sumab.append(sumab)
        dist=math.sqrt(sumab)
        Dist.append(dist)
##    print (Dist)
    a=(min(Dist))
##    print("yrchgj",a)
    for s in range (len(Dist)):
            if Dist[s]==a:
                n =s
                Y_p=ynew[n]
    pred_y.append(Y_p)
    print(pred_y)

err=[]
for i in range(len(y)):
    error=y[i]-pred_y[i]
    err.append(error)
print("error is",err)
c=10-sum(err)
print(c)
print("mean accuracy " ,((c/(len(err))*100))) 
