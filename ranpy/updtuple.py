n=int(input("enter number of ele:"))
values=[]
for i in range(n):
    values.append(int(input("enter element: ")))

t=tuple(values)
print("original tuple: ",t)

pos=int(input("enter index to update: "))
newval=int(input("enter new value: "))

values=list(t)
values[pos]=newval
t=tuple(values)

print("updated tuple= ",t)