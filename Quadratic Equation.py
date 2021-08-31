a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
x1 = (-b+D**0.5)/2 * a
x2 = (-b-D**0.5)/2 * a
if a == 0:
    print('Non-quadratic equation')
    if b != 0:
        print('One solution:', -(c/b))
    elif b == 0 and c != 0:
        print('No solutions')
    else:
        print('Infinite solutions')
elif a != 0:
    print('Quadratic equation')
    if D > 0:
        print('Discriminant:', D)
        print('Two solutions:', x1, x2)
    elif D == 0:
        print('One solution:', x1)
    else:
        print('Discriminant:', D)
        print('No solutions')


