

if __name__ == '__main__':
    N, K = map(int, input().split())
    S = input()
    ans = ''
    for i in range(N):
        if i == K-1:
            ans += S[i].lower()
        else:
            ans += S[i]

    print(ans)