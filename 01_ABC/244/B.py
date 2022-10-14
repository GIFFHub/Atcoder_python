N = int(input())
T = input()

flg = 0
x = 0
y = 0

for t in T:
    if t == 'S':
        if flg % 4 == 0:
            x += 1
        elif flg % 4== 1:
            y -= 1
        elif flg % 4 == 2:
            x -= 1
        else:
            y += 1
    else:
        flg += 1

print(x, y)