import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as m

df=pd.read_csv('E:\Book1.csv')

height=np.array(df['Height'])
label=np.array(df['Gender'])

mheight = sum(height)/len(height)
print ("height mean:", mheight)

mlabel = sum(label)/len(label)
print ("label mean:", mlabel)

slope = 0
bias = 0
for i in range(len(height)):
    slope += (height[i] - mheight) * (label[i] - mlabel)
    bias += (height[i] - mheight) ** 2                
            
b1 = slope / bias
b0 = mlabel - (b1 * mheight)


print ("Slope:", b1)
print ("Intercept:", b0)

y_pre=[]
sig=list()
for i in range(len(height)):
    y_pred = b0 + b1 * height[i]
    y_pre.append(y_pred)
    sigmoid=np.exp(y_pre)
    sigmoidd = (sigmoid/(1+sigmoid))
    sig.append(sigmoidd)   
    
print("y_pre is:",y_pre)
print("sig is:",sig)

threshold=0.5
for i in range(len(sig)):
    if np.any(sig[i]<=0.5):
        print("female")
    else:
        print("male")

plt.scatter(height,label,s=10)
plt.xlabel('height')
plt.ylabel('label')

plt.plot(height,y_pre,color='y')
plt.scatter(height,y_pre,color='r')
                 
plt.show()


     



    
        
    

