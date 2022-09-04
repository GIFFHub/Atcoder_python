import itertools

def judge(N, A_cum):
    for x in range(N):
        for y in range(x, N):
            if A_cum[y] - A_cum[x] > P:
                return 'No'
            if A_cum[y] - A_cum[x] == P:
                for z in range(y, N):
                    if A_cum[z] - A_cum[y] > Q:
                        return 'No'
                    if A_cum[z] - A_cum[y] == Q:
                        for w in range(z, N):
                            if A_cum[w] - A_cum[z] > R:
                                return 'No'
                            if A_cum[w] - A_cum[z] == R:
                                return 'Yes'

    return 'No'

if __name__ == '__main__':
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    A_cum = list(itertools.accumulate(A))
    print(judge(N, A_cum))



