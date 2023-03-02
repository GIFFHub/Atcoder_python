

if __name__ == '__main__':
    A = []
    for i in range(3):
        A.append(list(map(int, input().split())))
    card = [[0] * 3 for _ in range(3)]
    N = int(input())
    for _ in range(N):
        b = int(input())
        for i in range(3):
            for j in range(3):
                if A[i][j] == b:
                    card[i][j] = 1
    ans = 0
    # 横ビンゴ
    for i in range(3):
        if sum(card[i]) == 3:
            ans = 1

    # 縦ビンゴ
    for j in range(3):
        tmp = 0
        for i in range(3):
            tmp += card[i][j]
        if tmp == 3:
            ans = 1

    # 斜めビンゴ
    if card[0][0] + card[1][1] + card[2][2] == 3:
        ans = 1
    if card[0][2] + card[1][1] + card[2][0] == 3:
        ans = 1

    if ans:
        print('Yes')
    else:
        print('No')



