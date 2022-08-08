n = eval(input("Please enter a number "))


for y in range(1, n+1):
    currentLine = ""
    for x in range(1, y+1):
        currentLine += str(x)
    if y == n:
        for x in range(y-1, 0, -1):
            currentLine += str(x)
    else:
        for x in range(y, 0, -1):
            currentLine += str(x)
    print(currentLine)
