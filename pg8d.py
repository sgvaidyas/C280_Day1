import math
alist = []
n = int(input("Please enter a number    > "))
for i in range(n):
    if n-i == i+1:
        alist.append(str(n-i))
    else:
        alist.append(str(n - i))
        alist.append(str(i + 1))

    if i+1 >=n/2:
        break
print(" ".join(alist))
