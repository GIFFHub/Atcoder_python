

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    T = 10**18
    A.sort()
    if A[0] == 0:
        print(0)
    else:
        for a in A:
            ans *= a
            if ans > T:
                print(-1)
                break
        else:
            print(ans)