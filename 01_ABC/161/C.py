import math

if __name__ == '__main__':
    N, K = map(int, input().split())
    if N < K:
        if N >= K//2:
            print(K-N)
        else:
            print(N)
    else:
        # 初期値Nで、マイナスになるまで、Kずつ減る
        tmp = N % K
        if tmp == 0:
            print(0)
        else:
            tmp -= K
            print(abs(tmp))
