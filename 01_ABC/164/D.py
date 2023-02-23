from collections import defaultdict
import sys


if __name__ == '__main__':
    input = sys.stdin.readline
    S = int(input())
    M = 2*(10**5)+1
    keta = 0
    for i in range(M):
        if S // 10 ** i == 0:
            keta = i
            break

    T = 2019
    num = []
    for i in range(keta):
        #num.append(int(S[i:]) % 2019)
        tmp = S//(10**(keta-i))
        S -= tmp * (10**(keta-i))
        num.append(S % 2019)

    num.append(0)
    d = defaultdict(int)
    for n in num:
        d[n] += 1

    ans = 0
    for a in d.values():
        ans += a*(a-1)//2

    print(ans)






