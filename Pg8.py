num = int(input("Enter num = "))
a = []
for i in range(1,num+1):
    a.append(i)
# a = [1,2,3,4,5]
a_rev = list(reversed(a))
#a_rev = [5,4,3,2,1]
final = []
if num % 2 == 0:
    for i in range(int(len(a)/2)):# 0, 1 ,2
        final.append(a_rev[i])
        final.append(a[i])
else:
    centre_index = int((len(a)-1)/2) #3
    for i in range(int(   (len(a)-1) /2   )):
        final.append(a_rev[i])
        final.append(a[i])
    final.append(a_rev[centre_index])
print(final)
