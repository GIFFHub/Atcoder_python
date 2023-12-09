

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    P = list(map(int, input().split()))
    d = dict()
    kyori = [0]*(N-1) # A1までの距離
    # A1からの距離を求める
    for i in range(N-1):
        if P[i] == 1:
            kyori[i] = 1
        else:
            kyori[i] = kyori[P[i]-2] + 1
    #print(kyori)

    T = []
    len_kyori = len(kyori)
    for i in range(len_kyori):
        T.append((kyori[i], i))
    T.sort(reverse=True)
    #print(T)

    tmp_max_kyori = T[0][0]
    kasanchi = 0
    for i in range(len_kyori):
        if T[i][0] != tmp_max_kyori:
            if kasanchi > 0:
                print('+')
                exit()
            elif kasanchi < 0:
                print('-')
                exit()
            else:
                tmp_max_kyori = T[i][0]
        kasanchi += A[T[i][1]+1]

    if A[0] > 0:
        print('+')
    elif A[0] < 0:
        print('-')
    else:
        print(0)








