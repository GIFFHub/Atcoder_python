from collections import deque


if __name__ == '__main__':
    Q = int(input())
    d = deque()
    tmp = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            c = query[2]
            d.append((x, c))
        else:
            ans = 0
            c = query[1]
            while True:
                tmp = d.popleft()
                bias = tmp[1]-c # 今回取り出したボールと取り出し予定だったボール数の差

                # 予定通りの数を取り出した場合
                if bias == 0:
                    ans += tmp[0]*tmp[1]
                    print(ans)
                    break
                # 予定よりも多く取り出した場合
                # →戻す必要がある
                elif bias > 0:
                    ans += tmp[0]*(tmp[1]-bias)
                    print(ans)
                    # 多く取り出した分だけ戻す
                    d.appendleft((tmp[0], bias))
                    break
                # 予定よりも少なく取り出した場合
                # まだ取り出せる
                else:
                    ans += tmp[0]*tmp[1]
                    c -= tmp[1]






