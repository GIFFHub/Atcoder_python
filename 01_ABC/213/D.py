import sys

sys.setrecursionlimit(5000000)

def visit(current, prev):
    # 行った記録を残す
    ans.append(current+1)
    city[current] = False

    # 次に行く都市を探す
    for t in T[current]:
        # まだ行ってない都市を発見した場合
        if city[t]:
            visit(t, current)
    # 今の都市から行ける都市が全て行ったことある場合
    else:
        if current == 0:
            return
        else:
            ans.append(prev+1)
            return


if __name__ == '__main__':
    N = int(input())
    A = []
    B = []
    T = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        T[a-1].append(b-1)
        T[b-1].append(a-1)
    for i in range(N):
        T[i].sort()

    city = [True] * N # True: 行ったことない
    ans = []
    visit(0, 0)
    print(*ans)

