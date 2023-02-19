from collections import deque


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    S = set(A)
    ans = 0
    for i in range(K):
        if i in S:
            continue
        else:
            ans = i
            break
    else:
        ans = K

    print(ans)








