

if __name__ == '__main__':
    S = input()
    ans = 0
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            ans += 1

    print(ans)