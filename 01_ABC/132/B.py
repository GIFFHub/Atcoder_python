

if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N-2):
        T = [P[i], P[i+1], P[i+2]]
        min_T = min(T)
        max_T = max(T)
        if min_T < P[i+1] < max_T:
            ans += 1
        elif P[i+1] == max_T:
            if T.count(max_T) == 2:
                ans += 1

    print(ans)