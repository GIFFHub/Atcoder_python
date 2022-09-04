

if __name__ == '__main__':
    N = int(input())
    S = []
    ans = []
    for i in range(N):
        tmp = input()

        if tmp not in S:
            S.append(tmp)
            ans.append(i+1)

    for i in range(len(ans)):
        print(ans[i])





