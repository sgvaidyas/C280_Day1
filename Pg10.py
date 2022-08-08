n = int(input("Enter a num = "))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end="\t")
    print("\t" * (((2*n) - 1 ) - 2*row),end="")
    for col in range(row,0,-1):
        if col<n:
            print(col,end="\t")
    print()
