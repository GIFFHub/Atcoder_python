

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # R[i] : A[t] <= A[i]+K を満たす最大のt
    # A[i]から、どこまで、差がKを超えずにいけるか。（ギリギリの値がA[t]、つまりA[R[i]]
    # つまり、A[i]からみた、ギリギリのインデックスがR[i]

    # Aの各インデックスに対する、ギリギリのインデックス配列を初期化
    R = [None] * N

    # しゃくとり法
    for i in range(0, N-1):
        # スタート地点決める。
        if i == 0:
            R[i] = 0
        else:
            R[i] = R[i-1]

        # R[i] < N-1  :  ギリギリのインデックスが、右端まで行ってないか？
        # A[R[i]+1]-A[i] <= K  :  R[i]の次のインデックスは、A[i]との差がKを超えていないか？
        while R[i] < N-1 and A[R[i]+1]-A[i] <= K:
            # 上記条件を満たしていれば、R[i]を次にいってよし
            R[i] += 1

    ans = 0
    for i in range(N-1):
        # A[i]は、A[R[i]]まで差がKを超えない
        # R[i]-i　だけ、差がKを超えないindex間隔がある
        ans += R[i]-i

    print(ans)
