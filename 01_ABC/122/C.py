

if __name__ == '__main__':
    N, Q = map(int, input().split())
    S = input()
    T = [0]*N
    tmp = 0
    for i in range(1, N):
        if S[i-1]+S[i] == 'AC':
            tmp += 1
        T[i] = tmp

    for i in range(Q):
        l, r = map(int, input().split())
        print(T[r-1]-T[l-1])

