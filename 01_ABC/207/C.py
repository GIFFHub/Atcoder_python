
def check(pos1, pos2):
    if pos1[0] <= pos2[0] <= pos1[1]:
        return True
    if pos1[0] <= pos2[1] <= pos1[1]:
        return True
    if pos2[0] <= pos1[0] <= pos2[1]:
        return True
    return


if __name__ == '__main__':
    N = int(input())

    P = []
    for _ in range(N):
        t, l, r = map(int, input().split())
        if t == 1:
            P.append((l,r))
        elif t == 2:
            P.append((l,r-1/2))
        elif t == 3:
            P.append((l+1/2,r))
        elif t == 4:
            P.append((l+1/2,r-1/2))

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if check(P[i], P[j]):
                ans += 1

    print(ans)
