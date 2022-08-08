b = "burger"
p = "pizza"
pa = "pasta"

sel = str(input("please select if you want a burger, pizza or pasta"))

t = 0
if b or p or pa:
    b = input("how many burgers would you like")
    b = int(b)
    p = input("how many pizzas would you like")
    p = int(p)
    pa = input("how many portions of pasta would you like")
    pa = int(pa)
    t =+ (b*150) + (p*200) + (pa*180)
    print("your bill is", t)
else:
    print("the customer exited, total bill =", t)
