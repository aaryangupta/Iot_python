import numpy as np
import matplotlib.pyplot as plt

x = [1.0, 2.0, 4.0, 3.0, 5.0]
y = [1.0, 3.0, 3.0, 2.0, 5.0]

print ("X values:", x)
print ("Y values:", y)

avgx = sum(x)/len(x)
print ("x mean:", avgx)

avgy = sum(y)/len(y)
print ("y mean:", avgy)


slope = 0
bias = 0
for i in range(len(x)):
    slope += (x[i] - avgx) * (y[i] - avgy)
    bias += (x[i] - avgx) ** 2                
    print(slope)           
b1 = slope / bias
b0 = avgy - (b1 * avgx)

print ("Slope:", b1)
print ("Intercept:", b0)

rmse = 0
y_pre=[]
for i in range(len(x)):
    y_pred = b0 + b1 * x[i]
    rmse += (y[i] - y_pred) ** 2
    y_pre.append(y_pred)
rmse = np.sqrt(rmse/len(x))
print ("Rmse:", rmse)
print("y_pre is:",y_pre)

plt.scatter(x,y,s=10)
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,y_pre,color='y')
                 
plt.show()
