

if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    ans = []
    ans_index = []
    cnt = 0

    P_sort = sorted(P)

    while P != P_sort:
        for i in range(N-1):
            if i < N-2 and P[i] > P[i + 1] > P[i + 2]:
                P[i], P[i+2] = P[i+2], P[i]
                ans.append('B')
                ans_index.append(i)
                cnt += 1
            else:
                P[i], P[i+1] = P[i+1], P[i]
                ans.append('A')
                ans_index.append(i)
                cnt += 1

    print(cnt)
    for j in range(cnt):
        print(ans[j], ans_index[j])
