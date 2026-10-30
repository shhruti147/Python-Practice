s=input("enter string ")
s1=s
dict={}
for i in s:
    count=0
    for j in s1:
        if i==j:
            count=count+1
        dict[i]=count
print(dict)















s=input("enter str")
s1=s
dic={}
for i in s:
    count=0
    for j in s1:
        if i==j:
            count=count+1
            dic[i]=count

print(dic)
