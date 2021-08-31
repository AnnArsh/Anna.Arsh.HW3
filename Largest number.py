x = int(input())
while x > 0:
    if x < 10:
        print('n')
        break
    elif x % 10 < x//10 % 10:
        print('n')
        break
    else:
        print('y')
        break
