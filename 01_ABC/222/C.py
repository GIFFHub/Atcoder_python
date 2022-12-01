def check(id1, id2, m):
    a_id1 = A[id1-1][match-1]
    a_id2 = A[id2-1][match-1]
    if a_id1 == a_id2:
        return 0
    if a_id1 == 'G':
        if a_id2 == 'C':
            return 1
        else:
            return 2
    elif a_id1 == 'C':
        if a_id2 == 'P':
            return 1
        else:
            return 2
    elif a_id1 == 'P':
        if a_id2 == 'G':
            return 1
        else:
            return 2


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    for i in range(2*N):
        A.append(input())

    wins = [[] for _ in range(2*N)]
    for i in range(2*N):
        wins[i] = [0, i+1]

    for match in range(1, M+1):
        for p in range(1, N+1):
            fighter1_id = wins[2*p-1-1][1]
            fighter2_id = wins[2*p-1][1]

            winner = check(fighter1_id, fighter2_id, match)

            if winner == 1:
                wins[2*p-1-1][0] += 1
            elif winner == 2:
                wins[2*p-1][0] += 1
        wins.sort(key=lambda x: x[1])
        wins.sort(key=lambda x: x[0], reverse=True)
    for w in wins:
        print(w[1])



