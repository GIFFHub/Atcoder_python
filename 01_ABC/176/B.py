

if __name__ == '__main__':
    N = input()
    tmp = 0
    for n in N:
        tmp += int(n)

    if tmp % 9 == 0:
        print('Yes')
    else:
        print('No')
