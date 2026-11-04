s=input("Enter string: ")
old=input("enter char to replace: ")
new=input("enter replacement of above character")

replaced=lambda s:s.replace(old,new)
print("modified: ",replaced(s))