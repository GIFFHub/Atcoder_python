

if __name__ == '__main__':
    N, M = map(int, input().split())
    past = set()
    S = []
    for _ in range(N):
        S.append(input())

    for _ in range(M):
        t = input()
        past.add(t)

    ans = 0
    for s in S:
        if s[3:] in past:
            ans += 1

    print(ans)