import math

if __name__ == '__main__':
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    S.reverse()
    ans = 0
    for i in range(1, N+1):
        if S[i-1] == 'AND':
            pass
        else:
            ans += 2**(N-i+1)
    ans += 1

    print(ans)




