

if __name__ == '__main__':
    N = int(input())
    f = 0
    a = 0
    for _ in range(N):
        s = input()
        if s[0] == 'F':
            f += 1
        else:
            a += 1

    if f > a:
        print('Yes')
    else:
        print('No')

