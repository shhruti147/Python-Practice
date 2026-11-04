li=[]
r=int(input("enter range: "))
for i in range(r):
    x=input()
    li.append(x)
li2=[]
for i in li:
    if i not in li2:
        li2.append(i)
print(li2)