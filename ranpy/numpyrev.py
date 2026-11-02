import numpy as np
n=int(input("enter number of ele in array: "))
a=[]
for i in range(n):
    a.append(int(input("enter elements: ")))

b=[]
for i in range(n-1,-1,-1):
    b.append(a[i])

a=np.array(a)
b=np.array(b)
print("original",a)
print("rev: ",b)