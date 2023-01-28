

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    ans = 0
    for i, a in enumerate(A):
        ans -= a*(N-i-1)
        ans += a*i

    print(ans)



