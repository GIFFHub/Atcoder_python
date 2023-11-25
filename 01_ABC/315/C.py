from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    T = []
    for _ in range(N):
        f, s = map(int, input().split())
        T.append((s, f))

    T.sort(reverse=True)
    ans = T[0][0] + T[1][0]//2
    len_T = len(T)
    cnt = 1
    while True:
        if cnt == len_T:
            break
        if T[cnt][1] == T[0][1]:
            cnt += 1
        else:
            ans = max(ans, T[0][0]+T[cnt][0])
            break

    print(ans)









