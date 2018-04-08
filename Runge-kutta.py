import numpy as np

y=np.array([[1],[1]])

x=np.array([0])

h = 0.01

k11 = []

k21 = []

k31 = []

k41 = []

k12 = []

k22= []

k32 = []

k42 = []

for j in range (0, 5):
 l=h*y[1][j]
 k11.append(l)
 m=h*(y[1][j] + k11[j]/2)
 k21.append(m)
 n=h*(y[1][j] + k21[j]/2)
 k31.append(n)
 o=h*(y[1][j] + k31[j])
 k41.append(o)
 p=y[1][j]+(1/6)*(k11[j]+2*k21[j]+2*k31[j])+k41[j]
 
 l=h*(y[1][j]+y[0][j])
 k12.append(l)
 m=h*(y[1][j]+y[0][j] + k12[j]/2)
 k22.append(m)
 n=h*(y[1][j]+y[0][j]+ k22[j]/2)
 k32.append(n)
 o=h*(y[1][j]+y[0][j] + k32[j])
 k42.append(o)
 q=y[1][j]+(1/6)*(k12[j]+2*k22[j]+2*k32[j])+k42[j]
 
 y = np.append(y, [[p],[q]], axis=1)
 q=(j+1)*h
 x= np.append(x, q)

print(x)

print(y[0])
print(y[1])
