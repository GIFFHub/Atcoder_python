

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    M = max(A)
    top = 0
    ans = 0
    for k in range(2, M+1):
        tmp = 0
        for a in A:
            if a % k == 0:
                tmp += 1
        if top < tmp:
            top = tmp
            ans = k

    print(ans)

