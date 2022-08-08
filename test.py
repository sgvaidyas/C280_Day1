def function3():
    n = int(input("Number: "))
    a=[]
    if (n %2)==0:
        for i in range (n):
            if i <n:
                x = n-i
                a.append(x)
                a.append(i)
        numbers = n
        a=list(filter(lambda num: num != 0, a))
        print(a[0:numbers])
    else:
        print("Number is odd")
if __name__=="__main__":
    function3()
