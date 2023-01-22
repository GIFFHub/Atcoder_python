import math

if __name__ == '__main__':
    N = int(input())
    M = 10**5
    s = set()
    for a in range(2, M):
        for b in range(2, M):
            tmp = math.pow(a, b)
            if tmp <= N:
                s.add(tmp)
            else:
                break

    ans = N - len(s)

    print(ans)
