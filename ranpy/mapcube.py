n=int(input("how many num: "))
loti=[]
for i in range(n):
    x=int(input("enter nummber: "))
    loti.append(x)

result=list(map(lambda x: x ** 3,loti))

print("cubes",result)