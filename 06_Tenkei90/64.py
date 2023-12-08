if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    T = [0]*(N-1) # i項目とi+1項目の差
    for i in range(N-1):
        T[i] = A[i+1]-A[i]

    ans = 0
    for t in T:
        ans += abs(t)

    for i in range(Q):
        l, r, v = map(int, input().split())
        # l-1項目とl項目の差がv増える
        # r-1項目とr項目の差がv減る
        # l側の偏差
        if l != 1:
            ans += abs(T[l-2]+v) - abs(T[l-2])
            T[l-2] += v
        # r側の偏差
        if r != N:
            ans += abs(T[r-1]-v) - abs(T[r-1])
            T[r-1] -= v

        print(ans)

