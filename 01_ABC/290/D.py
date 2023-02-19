import math

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, D, K = map(int, input().split())
        g = math.gcd(N, D)

        n = N // g
        # n回でスタートラインに返ってくる
        # K回のうちに何回スタートラインに戻ってきたか
        # →その分右に1ずれる
        cir = (K-1) // n # 0地点に印をつけるためK-1

        # 最後の1周でどこまでいくか
        last = (K-1) * D % N

        print(cir+last)



