n = int(input("Please enter a number:   > "))
gaps = n * 2 - 1
aList = [" " for i in range(gaps)]
for i in range(n):
    aList[i] = str(i+1)
    aList[(len(aList)-1)-i] = str(i+1)
    print("".join(aList))
