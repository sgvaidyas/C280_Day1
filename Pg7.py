n = int(input("Enter the n = "))

reverse = reversed(range(1, n+1))

for i in range(1, n+1):
    rev = next(reverse)
    print(f"{i} * {rev} = {i * rev}")
