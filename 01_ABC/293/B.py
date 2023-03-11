

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    S = set()
    for i, a in enumerate(A):
        if i+1 not in S:
            S.add(a)

    ans = []
    for i, a in enumerate(A):
        if i+1 not in S:
            ans.append(i+1)

    ans.sort()
    print(len(ans))
    print(*ans)