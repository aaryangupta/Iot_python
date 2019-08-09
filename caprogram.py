import numpy as np
import matplotlib.pyplot as plt

x1=[2.7810836,1.465489372,3.396561688,1.38807019,3.06407232,7.627531214,5.332441248,6.922596716,8.6754418651,7.673756466]
x2=[2.550537003,2.362125076,4.400293529,1.850220317,3.005305973,2.759262235,2.088626775,1.77106367,-0.242068655,3.508563011]
y=[0,0,0,0,0,1,1,1,1,1]



l=0.3
epochs=10

b0=0
b1=0
b2=0

yp=list()
for i in range(epochs):
    for i in range(len(x1)):
        Y_pred=(b2*x2[i]+b1*x1[i]+b0)
        Y_pred = 1/(1+np.exp(-Y_pred))
        error1=Y_pred-y[i]
        b0=b0-l*error1
        b1=b1-l*error1*x1[i]
        print ("-----",b1)
        b2=b2-l*error1*x2[i]
        print ("-------",b2)
        #yp.append(Y_pred)
    print(b0,b1,b2)

ynew=[]  
signew=[]
y_p =list()
ne=list()
threshold=0.5
for i in range(10):
    ypred=b0+b1*x1[i]+b2*x2[i]
    ynew.append(ypred)
    sig = 1/(1+np.exp(-ypred))
    print (sig)
    signew.append(sig)
    
    #print("new error:",sum(ne))
    if(sig<=0.5):
        yp = 0
    else:
        yp = 1
    y_p.append(yp)
    newerror=yp-y[i]
    ne.append(newerror)

print (y, y_p, ne)

#total error
iterat = [1,2,3,4,5,6,7,8,9,10]

plt.plot(x1,y_p)
plt.plot(iterat,ne)
plt.show()
    

