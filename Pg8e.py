n = int(input("Enter value: ")) + 1
output = []
for i in range(1, n):
    output.append(n-i)
    output.append(i)
output = list(dict.fromkeys(output))
print(output)
