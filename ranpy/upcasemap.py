def uppercase(s):
    res= ""
    for ch in s:
        if 'a'<=ch<='z':
            res=res+chr(ord(ch)-32)
        else:
            res=res+ch
    return res

n=int(input("enter number"))
w=[]
for i in range(n):
    x=input("enter string ")
    w.append(x)
res=list(map(uppercase,w))
print("uppercase string ",res)
