from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    d = defaultdict(int)
    for _ in range(N):
        s = input()
        T = []
        for x in s:
            T.append(x)
        T.sort()
        n = ''.join(T)
        d[n] += 1

    ans = 0
    for value in d.values():
        ans += value*(value-1)//2

    print(ans)



