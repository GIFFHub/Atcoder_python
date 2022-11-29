
if __name__ == '__main__':
    N, M = map(int, input().split())
    B = [[] for _ in range(N)]
    for i in range(N):
        B[i] = list(map(int, input().split()))

    base = B[0][0]
    if M > 1:
        if not 1 <= base%7 <= 1+(7-M):
            print('No')
            exit()

    for i in range(N):
        for j in range(M):
            if B[i][j] == base+(i*7) + j:
                pass
            else:
                print('No')
                break
        else:
            continue
        break
    else:
        print('Yes')



