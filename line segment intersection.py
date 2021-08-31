a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
if a1 > b1:
    a1, b1 = b1, a1
if a2 > b2:
    a2, b2 = b2, a2
if (a1 < a2 and b1 < a2) or (a1 > b2 and b1 > b2):
    print(0)
elif a1 < a2 and b1 < b2:
    print(b1 - a2)
elif a1 > a2 and b1 > b2:
    print(b2-a1)
elif a1 < a2 < b1 and a1 < b2 < b1:
    print(b2-a2)
else:
    print(b1-a1)




