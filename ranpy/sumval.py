s1={}
r1=int(input("enter number of items: "))
print("enter items: ")
for i in range(r1):
    key=input("enter key: ")
    value=int(input("enter value: "))
    s1[key]=value
total=0
for i in s1:
    total=total+s1[i]

print("dictionary= ",s1)
print("sum of values= ",total)
