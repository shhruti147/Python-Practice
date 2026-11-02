def multi_list(list):
    result = 1
    for i in list:
        result *= i
    return result

list1=[]
r=int(input("how many elements you want to store"))

for i in range(r):
    a=int(input())
    list1.append(a)

print("Multi of all numbers: ",multi_list(list1))