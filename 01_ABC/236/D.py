
def func(cur, score):
    global ans
    if not cur:
        ans = max(ans, score)
        return

    x = cur[0]
    for i in range(1, len(cur)):
        y = cur[i]
        nxt = cur[1:i] + cur[i+1:]
        func(nxt, score^A[x-1][y-1-x])
    return


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    ans = 0
    func(list(range(1, 2*N+1)), 0)

    print(ans)