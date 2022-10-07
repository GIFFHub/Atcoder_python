
Q = int(input())
S = []

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        S.append(query[1])

    elif query[0] == 2:
        pass

    else:
        print(max(S) - min(S))