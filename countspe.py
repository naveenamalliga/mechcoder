a=str(input("enter the paragraph"))
c=0
b=0
v=len(a)
for i in a:
    if i.isdigit():
     c=c+1
    if i.isalpha():
     b=b+1
d=v-(c+b)
print(d)
