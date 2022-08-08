num = int(input("Enter Number: "))
n = num
list = []
numbers = f"{num} "
for i in range(1,n+1):
    n -= 1
    if n !=0 and i + n == num and (n not in list):
        if i!=n:
            list.extend([i,n])
        else:
            list.append(i)

for x in list:
    numbers += f"{x} "
print(numbers)
