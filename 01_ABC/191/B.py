from collections import deque

if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = deque()

    for a in A:
        if not a == X:
            ans.append(a)

    print(*ans)

