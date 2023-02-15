from collections import deque

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    tmp = A[0]
    for i in range(1, N):
        tmp ^= A[i]
    ans = []
    for a in A:
        ans.append(tmp^a)

    print(*ans)





