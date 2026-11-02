import numpy as np
n=int(input("enter number of ele in matrix"))

a=np.ones((n,n))

print("matrix")
print(a)

print("dimension ",a.ndim)
print("shape ",a.shape)
print("size",a.shape)
print("data type",a.dtype)
print("num of bytes",a.nbytes)