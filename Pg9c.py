def task5():
    inp = int(input("Choose a number:\n"))
    for i in range(inp+1):
        for x in range(1, i + 1):
            print(x, end="")
            print(" ", end="")
        if inp == i:
            i = i-1
        for x in range(i, 0, -1):
            print(x, end=" ")
        print("")


if __name__ == '__main__':
    task5()
