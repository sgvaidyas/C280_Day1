n =9
reverse = reversed(range(1, n+1))
output = []

for i in range(1, n//2+2):
    rev = next(reverse)
    if str(rev) not in output:
        output.append(str(rev))
    if str(i) not in output:
        output.append(str(i))
print(" ".join(output))
