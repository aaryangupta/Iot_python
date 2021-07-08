import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('E:\Book1.csv')

x=np.array(df['Height'])
y=np.array(df['Gender'])


b0 = 0
b1= 0

L = 0.001  
epochs = 250 
y_pre=[]

for i in range(epochs):
        Y_pred = b1*x[i]+b0
        y_pre.append(Y_pred)
        error=Y_pred-y[i]
        print (error)
        b0=b0-(L*error)
        b1=b1-(L*error*x[i])

    #print(b0,b1)
print(b0,b1)


rmse = 0

"""for i in range(len(x)):
    y_pred = b0 + b1 * x[i]
    rmse += (y[i] - y_pred) ** 2
    y_pre.append(y_pred)
rmse = np.sqrt(rmse/len(x))
print ("Rmse:", rmse)"""
print("y_pre is:",y_pre)     


plt.scatter(x,y,s=10)
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,y_pre,color='y')
                 
plt.show()

