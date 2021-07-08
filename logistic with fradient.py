import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m
df = pd.read_csv ('E:\Book1.csv')
height = np.array(df['Height'])
gender = np.array(df['Gender'])

b0 = 0
b1= 0

L = 0.01  
epochs = 25
yp =list()
for i in range(epochs):
    for i in range(len(height)):
        y= b1*height[i]+b0
        error=y-gender[i]
        print(error)
        b0=b0-(L*error)
        b1=b1-(L*error*height[i])
    print ("-------------")
    print(b0,b1)
print(b0,b1)


y_pre=[]
sigmoidnew = []
for i in range(len(height)):
    newy = b0 + b1 * height[i]
    y_pre.append(newy)
    sigmoid = np.exp(newy)
    sigmoidd = (sigmoid/(1+sigmoid))
    sigmoidnew.append(sigmoidd)
    #print(ynew)
print("y is",y_pre)
print("Sigmoid is",sigmoidnew)



threshold = 0.5

"""for i in range(len(sigmoidnew)):
    if(sigmoidnew[i]<=0.5):
        print("Female")
    else:
        print("Male")
"""        
plt.scatter(height,gender)
plt.plot(height,y_pre,  color = 'red')

plt.show()

