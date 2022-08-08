def task1():
    name = input("What is your name?\n")
    subject = input("Which subject is this?\n")
    m1 = float(input("What is your m1 mark\n"))
    m2 = float(input("What is your m2 mark\n"))
    m3 = float(input("What is your m3 mark\n"))

    print("Name: " + name)
    print("Subject: " + subject)
    if (m1 < 100 or m1 > 0) or (m2 < 100 or m2 > 0)(m3 < 100 or m3 > 0):
        total = m1 + m2 + m3
        print("Total: " + total)
        avg = total / 3
        print("Average: " + str(avg))
        if avg >= 70:
            print("You got an A!")
        elif avg >= 50:
            print("You got a B!")
        elif avg >= 35:
            print("You got a C!")
        else:
            print("You failed. :(")
    else:
        print("Invalid range of marks")


if __name__ == '__main__':
    task1()
