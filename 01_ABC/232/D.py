from collections import deque

if __name__ == '__main__':
    H, W = map(int, input().split())
    C = deque()
    # 上下反転して考える（右か下に移動できる）
    for i in range(H):
        C.append(input())

    ans = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            # 初期地点の場合
            if i == j == 0:
                if C[i][j] == '#':
                    ans[i][j] = 0
                else:
                    ans[i][j] = 1
            # 最上層の場合（左からしか移動できない）
            elif i == 0:
                if C[i][j] == '#':
                    ans[i][j] = 0
                else:
                    ans[i][j] = ans[i][j-1]
            # 最左層の場合（上からしか移動できない）
            elif j == 0:
                if C[i][j] == '#':
                    ans[i][j] = 0
                else:
                    ans[i][j] = ans[i-1][j]
            # それ以外
            else:
                if C[i][j] == '#':
                    ans[i][j] = 0
                else:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]

    answer = 1
    for i in range(H):
        for j in range(W):
            if ans[i][j] > 0:
                answer = max(answer, i+j+1)
    print(answer)
