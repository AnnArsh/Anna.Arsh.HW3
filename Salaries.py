x = int(input())
y = int(input())
z = int(input())

if x >= y and x >= z:
    print(x - z if z <= y else x - y)
elif y >= z:
    print(y - x if z >= x else y - z)
elif z >= x:
    print(z - y if y <= x else z - x)
