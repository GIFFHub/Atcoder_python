import itertools

if __name__ == '__main__':
    N = int(input())
    A = []
    d = dict()
    for _ in range(N):
        A.append(list(map(int, input().split())))

    M = int(input())

    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if x in d:
            d[x].add(y)
        else:
            d[x] = set()
            d[x].add(y)
        if y in d:
            d[y].add(x)
        else:
            d[y] = set()
            d[y].add(x)

    arr = list(itertools.permutations([x for x in range(N)]))
    ans = 100000
    for runners in arr:
        tmp_ans = 0
        for ku in range(N):
            current_runner = runners[ku]
            if ku != N-1:
                next_runner = runners[ku+1]
                if next_runner in d:
                    if current_runner in d[next_runner]:
                        break
            time = A[current_runner][ku]
            tmp_ans += time
        else:
            ans = min(ans, tmp_ans)
    if ans == 100000:
        print(-1)
    else:
        print(ans)









