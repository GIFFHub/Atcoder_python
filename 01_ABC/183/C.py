import itertools


if __name__ == '__main__':
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        T.append(list(map(int, input().split())))

    arr = list(itertools.permutations([x for x in range(1, N)]))

    ans = 0
    for pattern in arr:
        current_pos = 0
        cost = 0
        for next_pos in pattern:
            cost += T[current_pos][next_pos]
            current_pos = next_pos
            if cost > K:
                break
        cost += T[current_pos][0]
        if cost == K:
            ans += 1

    print(ans)
