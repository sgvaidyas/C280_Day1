number = int(input("enter n:"))
print(number)
first = 1
last = 1
prints = 1
for i in range(0,(number)):
  print((number+last)%number)
  prints = prints +1
  last = last + 1
  if(prints>(number-1)):
    break
  print((number - first)%number)
  prints = prints +1
  first = first + 1
  if(prints>(number-1)):
    break
