

if __name__ == '__main__':
    N = int(input())
    T = []
    for i in range(N):
        S = input()

        win = 0
        for s in S:
            if s == 'o':
                win += 1

        T.append((win, i+1))

    T = sorted(T, key=lambda x:(x[1]))
    T = sorted(T, key=lambda x:(x[0]), reverse=True)

    ans = []
    for t in T:
        ans.append(t[1])

    print(*ans)




