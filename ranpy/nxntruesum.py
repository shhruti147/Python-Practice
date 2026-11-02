import numpy as np

n=int(input("enter n: "))
a=np.zeros((n,n), dtype=int)

for i in range(n):
    for j in range(n):
        a[i][j]=int(input("enter elements "))
print("matrix")
print(a)

all_true=True
total=0


for i in range(n):
    for j in range(n):
        if a[i][j]==0:
            all_true=False
        total+=a[i][j]

print("evaluate true: ",all_true)
print("sum= ",total)