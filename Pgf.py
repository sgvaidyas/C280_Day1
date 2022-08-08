n = int(input("Enter value: "))

output = []
a = 0
while a < n / 2:
    output.append(n - a)
    a += 1
    if a<=n/2:
        output.append(a)
print(output)
