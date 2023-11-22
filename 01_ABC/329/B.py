

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    max_A = max(A)

    ans = 0
    for a in A:
        if a < max_A:
           ans = max(ans, a)

    print(ans)

