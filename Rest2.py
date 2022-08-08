pizza = 200
burger = 150
pasta = 180
total = 0
s = 0
while s != 1:
    print(f"Menu:\n(1) Pizza costs {pizza}\n(2) Burger costs {burger}\n(3) Pasta costs {pasta}")
    choice = int(input("Enter order number: "))
    if choice == 1:
        qty = int(input("Please enter quantity: "))
        total += pizza * qty
    elif choice == 2:
        qty = int(input("Please enter quantity: "))
        total += burger * qty
    elif choice == 3:
        qty = int(input("Please enter quantity: "))
        total += burger * qty
    else:
        print("Order invalid")

    cont = input("Would you like to continue? ").lower()
    if cont == "no" or cont == "n":
        s = 1

print(f"Your total bill is £{total}")
