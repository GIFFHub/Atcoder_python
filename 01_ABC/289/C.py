
from itertools import product

if __name__ == '__main__':
    N, M = map(int, input().split())
    C = []
    A = []
    for i in range(M):
        C.append(int(input()))
        A.append(list(map(int, input().split())))

    ans = 0
    for pro in product((0, 1), repeat=M):
        s = set()
        for i, p in enumerate(pro):
            if p == 1:
                for a in A[i]:
                    s.add(a)

        for x in range(1, N+1):
            if x not in s:
                break
        else:
            ans += 1

    print(ans)



