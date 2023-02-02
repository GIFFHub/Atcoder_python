import itertools

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    A_crr = list(itertools.accumulate(A))

    # それぞれの移動で最大の正の向きへの移動を調べる
    M = [-1*(10**18)]*N
    max_move = M[0]
    tmp = 0

    for i in range(N):
        tmp += A[i]
        max_move = max(max_move, tmp)
        M[i] = max_move

    # 実際に移動する
    ans = 0
    current_pos = 0
    for j in range(N):
        ans = max(ans, current_pos+M[j])
        current_pos += A_crr[j]

    print(ans)

