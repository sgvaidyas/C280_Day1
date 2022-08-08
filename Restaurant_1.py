def task2():
    totalCost = 0
    pizzaqnt = 0
    burgerqnt = 0
    pastaqnt = 0
    while True:
        order = int(input("Please select a number?\n1 - Pizza (200$)\n2 - Burger (150$)\n3 - Pasta (180)\n4 - Exit\n"))
        if order == 1:
            qnt = int(input("How many would you like?\n"))
            pizzaqnt += qnt
            totalCost += 200 * qnt
        elif order == 2:
            qnt = int(input("How many would you like?\n"))
            burgerqnt += qnt
            totalCost += 150 * qnt
        elif order == 3:
            qnt = int(input("How many would you like?\n"))
            pastaqnt += qnt
            totalCost += 180 * qnt
        elif order == 4:
            print("Thank you!")
            if(pizzaqnt > 0):
                print("Pizzas: " + str(pizzaqnt))
            if (burgerqnt > 0):
                print("Burgers: " + str(burgerqnt))
            if (pastaqnt > 0):
                print("Pastas: " + str(pastaqnt))
            if (pizzaqnt < 0 and burgerqnt < 0 and pastaqnt < 0):
                print("No items ordered")
            else:
                print("Your total is: " + str(totalCost) + "$")
            break
        else:
            "Invalid input"


if __name__ == '__main__':
    task2()
