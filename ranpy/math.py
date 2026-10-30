import math as m
n=float(input("enter number: "))
p=int(input("enter power: "))

if n<0:
    print("invalid data")

else:
    print("square root= ",m.sqrt(n))
    print("power= ",m.pow(n,p))
    print("ceiling= ",m.ceil(n))
    print("floor= ",m.floor(n))