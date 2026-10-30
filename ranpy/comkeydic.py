d1={}
d2={}
d3={}
r1=int(input("length of dictionary 1 : "))
print("enter ele of d1: ")
for i in range(r1):
    key=input("enter key: ")
    value=int(input("enter value: "))
    d1[key]=value

r2=int(input("length of dictionary 2 : "))
print("enter ele of d2: ")
for i in range(r2):
    key=input("enter key: ")
    value=int(input("enter value: "))
    d2[key]=value

for i in d1:
    d3[i]=d1[i]
for i in d2:
    if i in d3:
        d3[i]=d3[i]+d2[i]
    else:
        d3[i]=d2[i]
print(d3)