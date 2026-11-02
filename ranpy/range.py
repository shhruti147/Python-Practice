def check_range(n,start,end):
    if n>=start and n<=end:
        print("Number is in range")
    else:
        print("number not in range")

n=int(input("enter number: "))
start=int(input("enter start range: "))
end=int(input("enter end range: "))

check_range(n,start,end)