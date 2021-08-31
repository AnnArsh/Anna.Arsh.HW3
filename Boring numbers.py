x = int(input())
while x > 0:
    if x < 10:
        print('b')
        break
    elif x % 10 == x//10 % 10:
        x = x // 10
    else:
        print('i')
        break
