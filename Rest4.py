ordering = True

foodList = [["Pizza",200],["Burger",150],["Pasta",180]]
order = []
amount = 0
while ordering:

    for i in foodList:
        print(f"{foodList.index(i)+1} {i[0]} ({i[1]})")

    print(f"{len(foodList)+1} Exit")

    num = int(input("What would you like to do?"))
    if num != len(foodList)+1:
        print(f"You have chosen {foodList[num-1][0]}")
        qty = int(input("How many would you like?"))
        if qty > 0:
            for i in range(qty):
                order.append(foodList[num-1][0])
                amount += foodList[num-1][1]

    if num == len(foodList)+1:
        print("List of all the orders:")
        for i in foodList:
            if order.count(i[0]) >0:
                print(i[0], " £",order.count(i[0])*i[1])
        print("Total: £", amount)
        break
