s1=set()
s2=set()

r1=int(input("range of set1: "))
print("elements of set 1: ")
for i in range(r1):
    a=input()
    s1.add(a)

r2=int(input("range of set2: "))
print("elements of set 2: ")
for i in range(r2):
    a=input()
    s2.add(a)

print("A= ",s1)
print("B= ",s2)

union=set()
for i in s1:
    union.add(i)

for i in s2:
    union.add(i)

print("Union= ",union)

intersection=set()
for i in s1:
    if i in s2:
        intersection.add(i)

print(intersection)

diff=set()
for i in s1:
    if i not in s2:
        diff.add(i)
print(diff)

symdiff=set()
for i in s1:
    if i not in s2:
        symdiff.add(i)
for i in s2:
    if i not in s1:
        symdiff.add(i)

print(symdiff)