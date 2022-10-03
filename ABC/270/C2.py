import sys
sys.setrecursionlimit(10**7)


def dfs(a, b):
    if a == Y:
        exit(print(*ans))
    for to in arr[a]:
        if to == b:
            continue
        ans.append(to)
        dfs(to, a)
    ans.pop()

if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for i in range(N-1):
        U, V = map(int, input().split())
        arr[U].append(V)
        arr[V].append(U)

    print(arr)
    ans = [X]
    dfs(X, -1)

