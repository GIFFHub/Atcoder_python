

if __name__ == '__main__':
    L, R = map(int, input().split())

    final = min(R, L+4040)
    T = []

    for x in range(L, final+1):
        T.append(x % 2019)

    len_T = len(T)
    ans = 2020
    if len_T == 1:
        ans = (T[0]**2) % 2019
    else:
        for i in range(len_T):
            for j in range(i+1, len_T):
                ans = min(ans, (T[i]*T[j]) % 2019)
    print(ans)