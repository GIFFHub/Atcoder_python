

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = 0
    prev = -100
    for a in A:
        ans += B[a-1]
        if prev == a-1:
            ans += C[a-2]
        prev = a
    print(ans)

