
def check(K):
    len_K = len(K)
    for x in range(len_K//2):
        if K[x] != K[-1-x]:
            return False
    return True


if __name__ == '__main__':
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    flg = False
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            C = S[i] + S[j]
            if check(C):
                flg = True

    if flg:
        print('Yes')
    else:
        print('No')




