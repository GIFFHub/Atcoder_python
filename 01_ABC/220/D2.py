

def operation_f(x, y):
    return (x+y) % 10


def operation_g(x, y):
    return (x*y) % 10


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    dp_prev = [0 for _ in range(10)]
    dp_next = [0 for _ in range(10)]

    # 0番目の要素はA[0]にしかならないのでそれだけ場合の数は1
    dp_prev[A[0]] = 1

    for i in range(N-1):
        for j in range(10):
            dp_next[operation_f(j, A[i+1])] += dp_prev[j] % MOD
            dp_next[operation_g(j, A[i+1])] += dp_prev[j] % MOD
        dp_prev = dp_next.copy()
        dp_next = [0 for _ in range(10)]

    for ans in dp_prev:
        print(ans%MOD)




