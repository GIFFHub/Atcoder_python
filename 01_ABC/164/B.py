

if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    ans = 0
    while True:
        C -= B
        if C <= 0:
            ans = 0
            break
        A -= D
        if A <= 0:
            ans = 1
            break

    if ans:
        print('No')
    else:
        print('Yes')

