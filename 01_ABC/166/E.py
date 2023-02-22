from collections import defaultdict
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)

    ans = 0
    # b>aが前提
    # bを小さい値から全探索しながらaのd[i+a]を加算していくことで
    # b<aになることを防ぐ
    for i, a in enumerate(A):
        if i-a in d:
            ans += d[i-a]
        d[i+a] += 1


    print(ans)




