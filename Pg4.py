a = int(input("Enter the val of a = "))
b = int(input("Enter the val of b = "))
c = int(input("Enter the val of c = "))

if a>b:
    #a is greater
    if a>c:
        print(a," is greater")
    else:
        print(c, " is greater")
else:
    #b is greater
    if b>c:
        print(b, "is greater")
    else:
        print(c, "is greater")


