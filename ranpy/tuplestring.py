n=int(input("enter number of elements"))
t=()
for i in range(n):
    x=input("enter element: ")
    t=t+(x,)
    s=" "
for i in t:
    s=s+i
print("tuple: ",t)
print("string: ",s)