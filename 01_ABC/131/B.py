

if __name__ == '__main__':
    N, L = map(int, input().split())

    x = 1000
    p = 0
    for i in range(1, N+1):
        if x >= abs(L+i-1):
            x = abs(L+i-1)
            p = i
    aji = 0
    for j in range(1, N+1):
        if j == p:
            continue
        aji += (L+j-1)

    print(aji)


