from collections import defaultdict
import sys


if __name__ == '__main__':
    readline = sys.stdin.readline
    read = sys.stdin.read
    S = input()
    MOD = 2019
    cnt = 1
    tmp = 0
    d = [0] * MOD
    d[0] = 1
    # % MODするループは、対象全て%MODせよ！
    for s in reversed(S):
        tmp = (int(s)*cnt + tmp) % MOD
        cnt *= 10
        cnt %= MOD # これをやらないと値が大きくなりすぎてTLE！
        d[tmp] += 1

    ans = 0
    for a in d:
        ans += a*(a-1)//2

    print(ans)






