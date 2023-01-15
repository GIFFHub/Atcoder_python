

if __name__ == '__main__':
    N = int(input())
    S = input()

    for i in range(N-1):
        ans = 0
        while True:
            if S[ans] != S[ans+(i+1)]:
                ans += 1
            else:
                print(ans)
                break
            if ans + i + 1 == N:
                print(ans)
                break
