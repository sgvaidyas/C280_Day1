def task4():
    inp = int(input("Choose a number:\n"))
    numList = []
    for x in range(inp):
        numList.append(x+1)
    for x in range(inp):
        if(x % 2 == 0):
            print(numList[-1],end="\t")
            del numList[-1]
        else:
            print(numList[0],end="\t")
            del numList[0]

if __name__ == '__main__':
    task4()
