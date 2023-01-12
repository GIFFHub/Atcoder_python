
def func(rest, score):
    global ans
    if not rest:
        ans = max(ans, score)
        return

    x = rest[0]
    for i in range(1, len(rest)):
        # もし仮にy(ペアの2人目）にiを選んだ時
        y = rest[i]
        # もうiは選べなくなる
        nxt_rest = rest[1:i]+rest[i+1:]
        # xとyを選んだ場合の暫定スコアと、残り選べるメンバを次の関数に渡す
        func(nxt_rest, score ^ A[x-1][y-1-x])
        # 戻ってきたらy選び直し
    return


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    ans = 0

    func(list(range(1, 2*N+1)), 0)

    print(ans)
