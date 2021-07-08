import numpy as np

x1 = np.array([2.327868056, 3.032830419, 4.485465382, 3.684815246, 2.283558563, 7.807521179, 6.132998106, 7.514829366, 5.502385039, 7.43293235])
x2 = np.array([2.458016525, 3.170770366, 3.696728111, 3.846846973, 1.853215097, 3.290132136, 2.140563087, 2.107056961, 1.404002608, 4.236232628])
y = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])

L=0.45


b1=0.0
b2=0.0

t=1
epochs=16

for i in range(epochs):
       for i in range(10):
        output=y[i]*(b1*x1[i])+(b2*x2[i])
        if output<1:
            b1=((1-1/t)*b1)+(1/(L*t))*(y[i]*x1[i])
            b2=((1-1/t)*b2)+(1/(L*t))*(y[i]*x2[i])
        else:
            b1=(1-1/t)*b1
            b2=(1-1/t)*b2
         
        t=t+1
        print("b1",b1)
        print("b2",b2)

print(b1,b2)
        

for i in range(len(x1)):
     yp = b1*x1[i] + b2*x2[i]
     print("Y predicted :", yp)
     
     if(yp<0):
         print("-1")
         y_p= -1
     else:
         print("1")
         y_p = 1

     error=y[i]-y_p
print("Total Error is :", error)
